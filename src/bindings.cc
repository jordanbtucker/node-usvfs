#include "bindings.h"

Nan::Persistent<v8::FunctionTemplate> USVFS::constructor;

NAN_MODULE_INIT(USVFS::Init) {
	v8::Local<v8::FunctionTemplate> ctor = Nan::New<v8::FunctionTemplate>(USVFS::New);
	constructor.Reset(ctor);
	ctor->InstanceTemplate()->SetInternalFieldCount(1);
	ctor->SetClassName(Nan::New("USVFS").ToLocalChecked());

	Nan::SetPrototypeMethod(ctor, "clearMappings", ClearMappings);
	Nan::SetPrototypeMethod(ctor, "linkDirectory", LinkDirectory);
	Nan::SetPrototypeMethod(ctor, "linkFile", LinkDirectory);
	Nan::SetPrototypeMethod(ctor, "spawn", Spawn);

	target->Set(Nan::New("USVFS").ToLocalChecked(), ctor->GetFunction());
}

NAN_METHOD(USVFS::New) {
	if (!info.IsConstructCall()) {
		return Nan::ThrowError(Nan::New("USVFS::New called without new keyword.").ToLocalChecked());
	}

	if (info.Length() < 1) {
		return Nan::ThrowError(Nan::New("USVFS::New instanceName is required.").ToLocalChecked());
	}

	if (!info[0]->IsString()) {
		return Nan::ThrowError(Nan::New("USVFS::New instanceName must be a string.").ToLocalChecked());
	}

	USVFS* usvfs = new USVFS();
	usvfs->Wrap(info.Holder());

	USVFSInitParameters(&usvfs->params, *Nan::Utf8String(info[0]), false, LogLevel::Error, CrashDumpsType::None, "");
	CreateVFS(&usvfs->params);

	info.GetReturnValue().Set(info.Holder());
}

NAN_METHOD(USVFS::ClearMappings) {
	ClearVirtualMappings();

	info.GetReturnValue().SetUndefined();
}

LPWSTR toLPWSTR(v8::Local<v8::Value> value) {
	int n = MultiByteToWideChar(CP_UTF8, 0, *Nan::Utf8String(value), -1, NULL, 0);
	LPWSTR str = new TCHAR[n];
	MultiByteToWideChar(CP_UTF8, 0, *Nan::Utf8String(value), -1, str, n);
	return str;
}

NAN_METHOD(USVFS::LinkDirectory) {
	if (info.Length() < 2) {
		return Nan::ThrowError(Nan::New("USVFS::LinkDirectory src and dest are required.").ToLocalChecked());
	}

	if (!info[0]->IsString()) {
		return Nan::ThrowError(Nan::New("USVFS::LinkDirectory src must be a string.").ToLocalChecked());
	}

	if (!info[1]->IsString()) {
		return Nan::ThrowError(Nan::New("USVFS::LinkDirectory dest must be a string.").ToLocalChecked());
	}

	BOOL success = VirtualLinkDirectoryStatic(toLPWSTR(info[0]), toLPWSTR(info[1]), LINKFLAG_RECURSIVE);
	if (!success) {
		return Nan::ThrowError("Unable to link directory");
	}

	info.GetReturnValue().SetUndefined();
}

NAN_METHOD(USVFS::LinkFile) {
	if (info.Length() < 2) {
		return Nan::ThrowError(Nan::New("USVFS::LinkFile src and dest are required.").ToLocalChecked());
	}

	if (!info[0]->IsString()) {
		return Nan::ThrowError(Nan::New("USVFS::LinkFile src must be a string.").ToLocalChecked());
	}

	if (!info[1]->IsString()) {
		return Nan::ThrowError(Nan::New("USVFS::LinkFile dest must be a string.").ToLocalChecked());
	}

	BOOL success = VirtualLinkFile(toLPWSTR(info[0]), toLPWSTR(info[1]), NULL);
	if (!success) {
		return Nan::ThrowError("Unable to link file");
	}

	info.GetReturnValue().SetUndefined();
}

// Currently blocks thread, which is not Node-like.
NAN_METHOD(USVFS::Spawn) {
	if (info.Length() < 1) {
		return Nan::ThrowError(Nan::New("USVFS::Spawn commandLine is required.").ToLocalChecked());
	}

	if (!info[0]->IsString()) {
		return Nan::ThrowError(Nan::New("USVFS::Spawn commandLine must be a string.").ToLocalChecked());
	}

	STARTUPINFO si;
	ZeroMemory(&si, sizeof(si));
	si.cb = sizeof(si);

	PROCESS_INFORMATION pi;
	ZeroMemory(&pi, sizeof(pi));

	LPWSTR commandLine = toLPWSTR(info[0]);

	BOOL success = CreateProcessHooked(NULL, commandLine, NULL, NULL, FALSE, NULL, NULL, NULL, &si, &pi);
	if (!success) {
		int lastError = GetLastError();
		int n = snprintf(NULL, NULL, "USVFS::Spawn could not spawn. Error code %d", lastError);
		char* buffer = new char[n];
		sprintf(buffer, "USVFS::Spawn could not spawn (%d).", GetLastError());
		return Nan::ThrowError(Nan::New(buffer).ToLocalChecked());
	}

	WaitForSingleObject(pi.hProcess, INFINITE);

	CloseHandle(pi.hProcess);
	CloseHandle(pi.hThread);

	info.GetReturnValue().SetUndefined();
}

NAN_MODULE_INIT(InitModule) {
	USVFS::Init(target);
}

NODE_MODULE(bindings, InitModule);
