#include <nan.h>
#include <usvfs.h>
#include <usvfsparameters.h>

class USVFS : public Nan::ObjectWrap {
	USVFSParameters params;

public:
	static Nan::Persistent<v8::FunctionTemplate> constructor;
	static NAN_MODULE_INIT(Init);
	static NAN_METHOD(New);
	// static NAN_METHOD(Connect);
	// static NAN_METHOD(BlacklistExecutable);
	static NAN_METHOD(ClearMappings);
	static NAN_METHOD(LinkDirectory);
	static NAN_METHOD(LinkFile);
	static NAN_METHOD(Spawn);
};
