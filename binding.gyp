{
	"targets": [
		{
			"target_name": "asmjit",
			"type": "static_library",
			"defines": [
				"ASMJIT_STATIC",
				"_WINDOWS",
				"NDEBUG",
				"BOOST_CONFIG_SUPPRESS_OUTDATED_MESSAGE"
			],
			"include_dirs": [
				"deps/usvfs/asmjit/src/asmjit"
			],
			"sources": [
				"deps/usvfs/asmjit/src/asmjit/base/assembler.cpp",
				"deps/usvfs/asmjit/src/asmjit/base/compiler.cpp",
				"deps/usvfs/asmjit/src/asmjit/base/compilercontext.cpp",
				"deps/usvfs/asmjit/src/asmjit/base/constpool.cpp",
				"deps/usvfs/asmjit/src/asmjit/base/containers.cpp",
				"deps/usvfs/asmjit/src/asmjit/base/cpuinfo.cpp",
				"deps/usvfs/asmjit/src/asmjit/base/globals.cpp",
				"deps/usvfs/asmjit/src/asmjit/base/hlstream.cpp",
				"deps/usvfs/asmjit/src/asmjit/base/logger.cpp",
				"deps/usvfs/asmjit/src/asmjit/base/operand.cpp",
				"deps/usvfs/asmjit/src/asmjit/base/podvector.cpp",
				"deps/usvfs/asmjit/src/asmjit/base/runtime.cpp",
				"deps/usvfs/asmjit/src/asmjit/base/utils.cpp",
				"deps/usvfs/asmjit/src/asmjit/base/vmem.cpp",
				"deps/usvfs/asmjit/src/asmjit/base/zone.cpp",
				"deps/usvfs/asmjit/src/asmjit/x86/x86assembler.cpp",
				"deps/usvfs/asmjit/src/asmjit/x86/x86compiler.cpp",
				"deps/usvfs/asmjit/src/asmjit/x86/x86compilercontext.cpp",
				"deps/usvfs/asmjit/src/asmjit/x86/x86compilerfunc.cpp",
				"deps/usvfs/asmjit/src/asmjit/x86/x86inst.cpp",
				"deps/usvfs/asmjit/src/asmjit/x86/x86operand.cpp",
				"deps/usvfs/asmjit/src/asmjit/x86/x86operand_regs.cpp"
			],
			"configurations": {
				"Release": {
					"msvs_settings": {
						"VCCLCompilerTool": {
							"ExceptionHandling": 1,
							"RuntimeTypeInfo": "true"
						}
					},
					"msvs_configuration_attributes": {
						"CharacterSet": 1
					},
					"msbuild_toolset": "v141",
					"msvs_windows_target_platform_version": "10.0.16299.0"
				}
			}
		},
		{
			"target_name": "fmt",
			"type": "static_library",
			"defines": [
				"_WINDOWS",
				"NDEBUG",
				"BOOST_CONFIG_SUPPRESS_OUTDATED_MESSAGE"
			],
			"include_dirs": [
				"deps/usvfs/fmt"
			],
			"sources": [
				"deps/usvfs/fmt/fmt/format.cc",
				"deps/usvfs/fmt/fmt/ostream.cc",
				"deps/usvfs/fmt/fmt/posix.cc",
				"deps/usvfs/fmt/fmt/printf.cc"
			],
			"configurations": {
				"Release": {
					"msvs_settings": {
						"VCCLCompilerTool": {
							"ExceptionHandling": 1,
							"RuntimeTypeInfo": "true"
						}
					},
					"msvs_configuration_attributes": {
						"CharacterSet": 1
					},
					"msbuild_toolset": "v141",
					"msvs_windows_target_platform_version": "10.0.16299.0"
				}
			}
		},
		{
			"target_name": "spdlog",
			"type": "static_library",
			"defines": [
				"_WINDOWS",
				"NDEBUG",
				"BOOST_CONFIG_SUPPRESS_OUTDATED_MESSAGE"
			],
			"include_dirs": [
				"deps/usvfs/spdlog/include/spdlog"
			],
			"sources": [],
			"configurations": {
				"Release": {
					"msvs_settings": {
						"VCCLCompilerTool": {
							"ExceptionHandling": 1,
							"RuntimeTypeInfo": "true"
						}
					},
					"msvs_configuration_attributes": {
						"CharacterSet": 1
					},
					"msbuild_toolset": "v141",
					"msvs_windows_target_platform_version": "10.0.16299.0"
				}
			}
		},
		{
			"target_name": "udis86",
			"type": "static_library",
			"defines": [
				"_WINDOWS",
				"NDEBUG",
				"BOOST_CONFIG_SUPPRESS_OUTDATED_MESSAGE"
			],
			"include_dirs": [
				"deps/usvfs/udis86"
			],
			"sources": [
				"deps/usvfs/udis86/libudis86/decode.c",
				"deps/usvfs/udis86/libudis86/itab.c",
				"deps/usvfs/udis86/libudis86/syn-att.c",
				"deps/usvfs/udis86/libudis86/syn-intel.c",
				"deps/usvfs/udis86/libudis86/syn.c",
				"deps/usvfs/udis86/libudis86/udis86.c"
			],
			"configurations": {
				"Release": {
					"msvs_settings": {
						"VCCLCompilerTool": {
							"ExceptionHandling": 1,
							"RuntimeTypeInfo": "true"
						}
					},
					"msvs_configuration_attributes": {
						"CharacterSet": 1
					},
					"msbuild_toolset": "v141",
					"msvs_windows_target_platform_version": "10.0.16299.0"
				}
			}
		},
		{
			"target_name": "shared",
			"type": "static_library",
			"dependencies": [
				"fmt",
				"spdlog"
			],
			"defines": [
				"_WIN64",
				"SPDLOG_NO_NAME",
				"SPDLOG_NO_REGISTRY_MUTEX",
				"NOMINMAX",
				"_WINDOWS",
				"NDEBUG",
				"BOOST_CONFIG_SUPPRESS_OUTDATED_MESSAGE"
			],
			"libraries": [
				"../deps/boost/stage/lib/libboost_atomic-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_atomic-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_chrono-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_chrono-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_context-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_context-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_coroutine-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_coroutine-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_date_time-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_date_time-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_filesystem-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_filesystem-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_locale-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_locale-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_log-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_log-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_log_setup-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_log_setup-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_regex-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_regex-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_system-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_system-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_thread-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_thread-vc141-mt-sgd-x64-1_67.lib"
			],
			"include_dirs": [
				"deps/usvfs/src/shared",
				"deps/usvfs/include",
				"deps/boost",
				"deps/usvfs/fmt",
				"deps/usvfs/spdlog/include/spdlog"
			],
			"sources": [
				"deps/usvfs/src/shared/addrtools.cpp",
				"deps/usvfs/src/shared/debug_monitor.cpp",
				"deps/usvfs/src/shared/directory_tree.cpp",
				"deps/usvfs/src/shared/exceptionex.cpp",
				"deps/usvfs/src/shared/loghelpers.cpp",
				"deps/usvfs/src/shared/ntdll_declarations.cpp",
				"deps/usvfs/src/shared/scopeguard.cpp",
				"deps/usvfs/src/shared/shmlogger.cpp",
				"deps/usvfs/src/shared/stringcast_win.cpp",
				"deps/usvfs/src/shared/stringutils.cpp",
				"deps/usvfs/src/shared/test_helpers.cpp",
				"deps/usvfs/src/shared/unicodestring.cpp",
				"deps/usvfs/src/shared/wildcard.cpp",
				"deps/usvfs/src/shared/winapi.cpp",
				"deps/usvfs/src/shared/windows_error.cpp"
			],
			"configurations": {
				"Release": {
					"msvs_settings": {
						"VCCLCompilerTool": {
							"ExceptionHandling": 1,
							"RuntimeTypeInfo": "true"
						}
					},
					"msvs_configuration_attributes": {
						"CharacterSet": 1
					},
					"msbuild_toolset": "v141",
					"msvs_windows_target_platform_version": "10.0.16299.0"
				}
			}
		},
		{
			"target_name": "thooklib",
			"type": "static_library",
			"dependencies": [
				"asmjit",
				"shared",
				"spdlog"
			],
			"defines": [
				"_WIN64",
				"ASMJIT_STATIC",
				"SPDLOG_NO_NAME",
				"SPDLOG_NO_REGISTRY_MUTEX",
				"NOMINMAX",
				"_WINDOWS",
				"NDEBUG",
				"BOOST_CONFIG_SUPPRESS_OUTDATED_MESSAGE"
			],
			"libraries": [
				"../deps/boost/stage/lib/libboost_atomic-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_atomic-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_chrono-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_chrono-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_context-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_context-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_coroutine-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_coroutine-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_date_time-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_date_time-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_filesystem-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_filesystem-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_locale-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_locale-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_log-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_log-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_log_setup-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_log_setup-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_regex-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_regex-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_system-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_system-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_thread-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_thread-vc141-mt-sgd-x64-1_67.lib"
			],
			"include_dirs": [
				"deps/usvfs/src/thooklib",
				"deps/usvfs/src/shared",
				"deps/usvfs/src/tinjectlib",
				"deps/usvfs/src/usvfs_helper",
				"deps/usvfs/asmjit/src/asmjit",
				"deps/usvfs/udis86",
				"deps/usvfs/include",
				"deps/boost",
				"deps/usvfs/fmt",
				"deps/usvfs/spdlog/include/spdlog"
			],
			"sources": [
				"deps/usvfs/src/thooklib/hooklib.cpp",
				"deps/usvfs/src/thooklib/ttrampolinepool.cpp",
				"deps/usvfs/src/thooklib/udis86wrapper.cpp",
				"deps/usvfs/src/thooklib/utility.cpp"
			],
			"configurations": {
				"Release": {
					"msvs_settings": {
						"VCCLCompilerTool": {
							"ExceptionHandling": 1,
							"RuntimeTypeInfo": "true"
						}
					},
					"msvs_configuration_attributes": {
						"CharacterSet": 1
					},
					"msbuild_toolset": "v141",
					"msvs_windows_target_platform_version": "10.0.16299.0"
				}
			}
		},
		{
			"target_name": "tinjectlib",
			"type": "static_library",
			"dependencies": [
				"asmjit",
				"shared"
			],
			"defines": [
				"_WIN64",
				"ASMJIT_STATIC",
				"SPDLOG_NO_NAME",
				"SPDLOG_NO_REGISTRY_MUTEX",
				"NOMINMAX",
				"_WINDOWS",
				"NDEBUG",
				"BOOST_CONFIG_SUPPRESS_OUTDATED_MESSAGE"
			],
			"libraries": [
				"../deps/boost/stage/lib/libboost_atomic-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_atomic-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_chrono-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_chrono-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_context-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_context-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_coroutine-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_coroutine-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_date_time-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_date_time-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_filesystem-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_filesystem-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_locale-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_locale-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_log-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_log-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_log_setup-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_log_setup-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_regex-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_regex-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_system-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_system-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_thread-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_thread-vc141-mt-sgd-x64-1_67.lib"
			],
			"include_dirs": [
				"deps/usvfs/src/tinjectlib",
				"deps/usvfs/src/shared",
				"deps/usvfs/src/thooklib",
				"deps/usvfs/src/usvfs_helper",
				"deps/usvfs/asmjit/src/asmjit",
				"deps/usvfs/udis86",
				"deps/usvfs/include",
				"deps/boost",
				"deps/usvfs/fmt",
				"deps/usvfs/spdlog/include/spdlog"
			],
			"sources": [
				"deps/usvfs/src/tinjectlib/injectlib.cpp"
			],
			"configurations": {
				"Release": {
					"msvs_settings": {
						"VCCLCompilerTool": {
							"ExceptionHandling": 1,
							"RuntimeTypeInfo": "true"
						}
					},
					"msvs_configuration_attributes": {
						"CharacterSet": 1
					},
					"msbuild_toolset": "v141",
					"msvs_windows_target_platform_version": "10.0.16299.0"
				}
			}
		},
		{
			"target_name": "usvfs_helper",
			"type": "static_library",
			"dependencies": [
				"shared",
				"tinjectlib"
			],
			"defines": [
				"BUILDING_USVFS_DLL",
				"_WIN64",
				"ASMJIT_STATIC",
				"SPDLOG_NO_NAME",
				"SPDLOG_NO_REGISTRY_MUTEX",
				"NOMINMAX",
				"_WINDOWS",
				"NDEBUG",
				"BOOST_CONFIG_SUPPRESS_OUTDATED_MESSAGE"
			],
			"libraries": [
				"../deps/boost/stage/lib/libboost_atomic-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_atomic-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_chrono-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_chrono-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_context-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_context-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_coroutine-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_coroutine-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_date_time-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_date_time-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_filesystem-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_filesystem-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_locale-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_locale-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_log-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_log-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_log_setup-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_log_setup-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_regex-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_regex-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_system-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_system-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_thread-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_thread-vc141-mt-sgd-x64-1_67.lib"
			],
			"include_dirs": [
				"deps/usvfs/src/usvfs_helper",
				"deps/usvfs/src/shared",
				"deps/usvfs/src/thooklib",
				"deps/usvfs/src/tinjectlib",
				"deps/usvfs/asmjit/src/asmjit",
				"deps/usvfs/udis86",
				"deps/usvfs/include",
				"deps/boost",
				"deps/usvfs/fmt",
				"deps/usvfs/spdlog/include/spdlog"
			],
			"sources": [
				"deps/usvfs/src/usvfs_helper/inject.cpp"
			],
			"configurations": {
				"Release": {
					"msvs_settings": {
						"VCCLCompilerTool": {
							"ExceptionHandling": 1,
							"RuntimeTypeInfo": "true"
						}
					},
					"msvs_configuration_attributes": {
						"CharacterSet": 1
					},
					"msbuild_toolset": "v141",
					"msvs_windows_target_platform_version": "10.0.16299.0"
				}
			}
		},
		{
			"target_name": "usvfs_x64",
			"type": "shared_library",
			"dependencies": [
				"asmjit",
				"fmt",
				"shared",
				"spdlog",
				"thooklib",
				"tinjectlib",
				"udis86",
				"usvfs_helper"
			],
			"defines": [
				"BUILDING_USVFS_DLL",
				"ASMJIT_STATIC",
				"SPDLOG_NO_NAME",
				"SPDLOG_NO_REGISTRY_MUTEX",
				"NOMINMAX",
				"_WINDOWS",
				"NDEBUG",
				"BOOST_CONFIG_SUPPRESS_OUTDATED_MESSAGE"
			],
			"libraries": [
				"Shlwapi.lib",
				"Version.lib",
				"../deps/boost/stage/lib/libboost_atomic-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_atomic-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_chrono-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_chrono-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_context-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_context-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_coroutine-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_coroutine-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_date_time-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_date_time-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_filesystem-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_filesystem-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_locale-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_locale-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_log-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_log-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_log_setup-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_log_setup-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_regex-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_regex-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_system-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_system-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_thread-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_thread-vc141-mt-sgd-x64-1_67.lib"
			],
			"include_dirs": [
				"deps/usvfs/include",
				"deps/usvfs/src/usvfs_dll",
				"deps/usvfs/src/shared",
				"deps/usvfs/src/thooklib",
				"deps/usvfs/src/tinjectlib",
				"deps/usvfs/src/usvfs_helper",
				"deps/usvfs/asmjit/src/asmjit",
				"deps/usvfs/udis86",
				"deps/boost",
				"deps/usvfs/fmt",
				"deps/usvfs/spdlog/include/spdlog"
			],
			"sources": [
				"deps/usvfs/src/usvfs_dll/hookcallcontext.cpp",
				"deps/usvfs/src/usvfs_dll/hookcontext.cpp",
				"deps/usvfs/src/usvfs_dll/hookmanager.cpp",
				"deps/usvfs/src/usvfs_dll/hooks/kernel32.cpp",
				"deps/usvfs/src/usvfs_dll/hooks/ntdll.cpp",
				"deps/usvfs/src/usvfs_dll/redirectiontree.cpp",
				"deps/usvfs/src/usvfs_dll/semaphore.cpp",
				"deps/usvfs/src/usvfs_dll/stringcast_boost.cpp",
				"deps/usvfs/src/usvfs_dll/usvfs.cpp"
			],
			"configurations": {
				"Release": {
					"msvs_settings": {
						"VCCLCompilerTool": {
							"ExceptionHandling": 1,
							"RuntimeTypeInfo": "true"
						}
					},
					"msvs_configuration_attributes": {
						"CharacterSet": 1
					},
					"msbuild_toolset": "v141",
					"msvs_windows_target_platform_version": "10.0.16299.0"
				}
			}
		},
		{
			"target_name": "usvfs_proxy",
			"type": "executable",
			"dependencies": [
				"asmjit",
				"shared",
				"tinjectlib",
				"usvfs_x64",
				"usvfs_helper"
			],
			"defines": [
				"_WIN64",
				"ASMJIT_STATIC",
				"SPDLOG_NO_NAME",
				"SPDLOG_NO_REGISTRY_MUTEX",
				"NOMINMAX",
				"_WINDOWS",
				"NDEBUG",
				"BOOST_CONFIG_SUPPRESS_OUTDATED_MESSAGE"
			],
			"libraries": [
				"../deps/boost/stage/lib/libboost_atomic-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_atomic-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_chrono-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_chrono-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_context-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_context-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_coroutine-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_coroutine-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_date_time-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_date_time-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_filesystem-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_filesystem-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_locale-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_locale-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_log-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_log-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_log_setup-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_log_setup-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_regex-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_regex-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_system-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_system-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_thread-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_thread-vc141-mt-sgd-x64-1_67.lib"
			],
			"include_dirs": [
				"deps/usvfs/src/shared",
				"deps/usvfs/src/thooklib",
				"deps/usvfs/src/tinjectlib",
				"deps/usvfs/src/usvfs_helper",
				"deps/usvfs/asmjit/src/asmjit",
				"deps/usvfs/udis86",
				"deps/usvfs/include",
				"deps/boost",
				"deps/usvfs/fmt",
				"deps/usvfs/spdlog/include/spdlog"
			],
			"sources": [
				"deps/usvfs/src/usvfs_proxy/main.cpp"
			],
			"configurations": {
				"Release": {
					"msvs_settings": {
						"VCCLCompilerTool": {
							"ExceptionHandling": 1,
							"RuntimeTypeInfo": "true"
						}
					},
					"msvs_configuration_attributes": {
						"CharacterSet": 1
					},
					"msbuild_toolset": "v141",
					"msvs_windows_target_platform_version": "10.0.16299.0"
				}
			}
		},
		{
			"target_name": "bindings",
			"dependencies": [
				"usvfs_x64"
			],
			"defines": [
				"BUILDING_USVFS_DLL",
				"ASMJIT_STATIC",
				"SPDLOG_NO_NAME",
				"SPDLOG_NO_REGISTRY_MUTEX",
				"NOMINMAX",
				"_WINDOWS",
				"NDEBUG",
				"BOOST_CONFIG_SUPPRESS_OUTDATED_MESSAGE"
			],
			"libraries": [
				"Shlwapi.lib",
				"Version.lib",
				"../deps/boost/stage/lib/libboost_atomic-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_atomic-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_chrono-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_chrono-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_context-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_context-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_coroutine-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_coroutine-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_date_time-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_date_time-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_filesystem-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_filesystem-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_locale-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_locale-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_log-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_log-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_log_setup-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_log_setup-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_regex-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_regex-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_system-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_system-vc141-mt-sgd-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_thread-vc141-mt-s-x64-1_67.lib",
				"../deps/boost/stage/lib/libboost_thread-vc141-mt-sgd-x64-1_67.lib"
			],
			"include_dirs": [
				"src",
				"<!(node -e \"require('nan')\")",
				"deps/usvfs/include",
				"deps/usvfs/src/usvfs_dll",
				"deps/usvfs/src/shared",
				"deps/usvfs/src/thooklib",
				"deps/usvfs/src/tinjectlib",
				"deps/usvfs/src/usvfs_helper",
				"deps/usvfs/asmjit/src/asmjit",
				"deps/usvfs/udis86",
				"deps/boost",
				"deps/usvfs/fmt",
				"deps/usvfs/spdlog/include/spdlog"
			],
			"sources": [
				"src/bindings.cc"
			],
			"configurations": {
				"Release": {
					"msvs_settings": {
						"VCCLCompilerTool": {
							"ExceptionHandling": 1,
							"RuntimeTypeInfo": "true"
						}
					},
					"msvs_configuration_attributes": {
						"CharacterSet": 1
					},
					"msbuild_toolset": "v141",
					"msvs_windows_target_platform_version": "10.0.16299.0"
				}
			}
		}
	]
}
