{
  'includes': [
    '../build/common.gypi',
  ],
  'variables': {
    'conditions': [
      ['OS=="android" or OS=="linux"', {
        'java_home%': '<!(python -c "import os; dir=os.getenv(\'JAVA_HOME\', \'/usr/lib/jvm/java-7-openjdk-amd64\'); assert os.path.exists(os.path.join(dir, \'include/jni.h\')), \'Point \\$JAVA_HOME or the java_home gyp variable to a directory containing include/jni.h!\'; print dir")',
      }],
      ['OS == "win"', {
        'peeracle_dir': '<!(python build\\get_current_dir.py)\\peeracle',
        'webrtc_dir': '<!(python build\\get_current_dir.py)\\..\\third_party\\webrtc',
      }, {
        'peeracle_dir': '<!(pwd)/peeracle',
        'webrtc_dir': '<!(pwd)/../third_party/webrtc',
      }],
    ],
  },
  'targets': [
    {
      'target_name': 'peeracle',
      'type': 'static_library',
      'cflags': [
        '-std=c++11',
        '-fPIC'
      ],
      'sources': [
        'lib/createanswerobserver.cc',
        'lib/createofferobserver.cc',
        'lib/createsessiondescriptionobserver.cc',
        'lib/manager.cc',
        'lib/peer.cc',
        'lib/setanswerobserver.cc',
        'lib/setlocalofferobserver.cc',
        'lib/setremoteofferobserver.cc',
        'lib/setsessiondescriptionobserver.cc',
      ],
      'include_dirs': [
        '<(webrtc_dir)',
        '<(webrtc_dir)/third_party',
      ],
      'conditions': [
        ['OS == "win"', {
          'defines': [
            'WEBRTC_WIN',
          ],
          'msvs_settings': {
            'VCCLCompilerTool': {
              'RuntimeLibrary': 0,
            },
          },
          'link_settings': {
            'libraries': [
              '<!@(python build\\find_libs.py <(webrtc_dir)\\out\\<(configuration))',
              '-ladvapi32.lib',
              '-lamstrmid.lib',
              '-ldmoguids.lib',
              '-lmsdmo.lib',
              '-lole32.lib',
              '-lsecur32.lib',
              '-lshell32.lib',
              '-lstrmiids.lib',
              '-lwmcodecdspuuid.lib',
            ],
          },
        }, {
          'defines': [
            'WEBRTC_POSIX',
          ],
        }],
        ['OS == "linux"', {
          'defines': [
            'WEBRTC_LINUX'
          ],
          'link_settings': {
            'libraries': [
              '-Wl,--start-group',
              '<!@(find <(webrtc_dir)/out/<(configuration) -name *.a -type f)',
              '-lpthread',
              '-ldl',
              '-lnss3',
              '-lnssutil3',
              '-lplc4',
              '-lnspr4',
              '-lX11',
              '-Wl,--end-group'
            ],
          },
        }],
        ['OS == "mac"', {
          'link_settings': {
            'libraries': [
              '-framework AVFoundation',
              '-framework Cocoa',
              '-framework Foundation',
              '-framework IOKit',
              '-framework Security',
              '-framework SystemConfiguration',
              '-weak_framework AVFoundation',
              '-framework CoreAudio',
              '-framework CoreVideo',
              '-framework OpenGL',
              '-framework QTKit',
              '-framework CFNetwork',
#              '<(webrtc_dir)/out/<(configuration)/libapprtc_signaling.a',
              '<(webrtc_dir)/out/<(configuration)/libjingle_peerconnection.a',
              '<(webrtc_dir)/out/<(configuration)/librtc_base.a',
              '<(webrtc_dir)/out/<(configuration)/libwebrtc_common.a',
              '<(webrtc_dir)/out/<(configuration)/librtc_base_approved.a',
              '<(webrtc_dir)/out/<(configuration)/libjsoncpp.a',
              '<(webrtc_dir)/out/<(configuration)/libboringssl.a',
              '<(webrtc_dir)/out/<(configuration)/libexpat.a',
              '<(webrtc_dir)/out/<(configuration)/libjingle_media.a',
              '<(webrtc_dir)/out/<(configuration)/libvideo_render_module.a',
              '<(webrtc_dir)/out/<(configuration)/libwebrtc_utility.a',
              '<(webrtc_dir)/out/<(configuration)/libaudio_coding_module.a',
              '<(webrtc_dir)/out/<(configuration)/libCNG.a',
              '<(webrtc_dir)/out/<(configuration)/libcommon_audio.a',
              '<(webrtc_dir)/out/<(configuration)/libsystem_wrappers.a',
              '<(webrtc_dir)/out/<(configuration)/libopenmax_dl.a',
              '<(webrtc_dir)/out/<(configuration)/libcommon_audio_sse2.a',
              '<(webrtc_dir)/out/<(configuration)/libaudio_encoder_interface.a',
              '<(webrtc_dir)/out/<(configuration)/libG711.a',
              '<(webrtc_dir)/out/<(configuration)/libG722.a',
              '<(webrtc_dir)/out/<(configuration)/libiLBC.a',
              '<(webrtc_dir)/out/<(configuration)/libiSAC.a',
              '<(webrtc_dir)/out/<(configuration)/libaudio_decoder_interface.a',
              '<(webrtc_dir)/out/<(configuration)/libiSACFix.a',
              '<(webrtc_dir)/out/<(configuration)/libPCM16B.a',
              '<(webrtc_dir)/out/<(configuration)/libred.a',
              '<(webrtc_dir)/out/<(configuration)/libwebrtc_opus.a',
              '<(webrtc_dir)/out/<(configuration)/libopus.a',
              '<(webrtc_dir)/out/<(configuration)/libneteq.a',
              '<(webrtc_dir)/out/<(configuration)/libmedia_file.a',
              '<(webrtc_dir)/out/<(configuration)/libcommon_video.a',
              '<(webrtc_dir)/out/<(configuration)/libyuv.a',
              '<(webrtc_dir)/out/<(configuration)/libjpeg_turbo.a',
              '<(webrtc_dir)/out/<(configuration)/libwebrtc.a',
              '<(webrtc_dir)/out/<(configuration)/libvideo_engine_core.a',
              '<(webrtc_dir)/out/<(configuration)/librtp_rtcp.a',
              '<(webrtc_dir)/out/<(configuration)/libpaced_sender.a',
              '<(webrtc_dir)/out/<(configuration)/libremote_bitrate_estimator.a',
              '<(webrtc_dir)/out/<(configuration)/libbitrate_controller.a',
              '<(webrtc_dir)/out/<(configuration)/libvideo_capture_module.a',
              '<(webrtc_dir)/out/<(configuration)/libwebrtc_video_coding.a',
              '<(webrtc_dir)/out/<(configuration)/libwebrtc_i420.a',
              '<(webrtc_dir)/out/<(configuration)/libvideo_coding_utility.a',
              '<(webrtc_dir)/out/<(configuration)/libwebrtc_vp8.a',
              '<(webrtc_dir)/out/<(configuration)/libvpx.a',
              '<(webrtc_dir)/out/<(configuration)/libvpx_intrinsics_mmx.a',
              '<(webrtc_dir)/out/<(configuration)/libvpx_intrinsics_sse2.a',
              '<(webrtc_dir)/out/<(configuration)/libvpx_intrinsics_ssse3.a',
              '<(webrtc_dir)/out/<(configuration)/libvpx_intrinsics_sse4_1.a',
              '<(webrtc_dir)/out/<(configuration)/libvpx_intrinsics_avx2.a',
              '<(webrtc_dir)/out/<(configuration)/libwebrtc_vp9.a',
              '<(webrtc_dir)/out/<(configuration)/libvideo_processing.a',
              '<(webrtc_dir)/out/<(configuration)/libvideo_processing_sse2.a',
              '<(webrtc_dir)/out/<(configuration)/libvoice_engine.a',
              '<(webrtc_dir)/out/<(configuration)/libaudio_conference_mixer.a',
              '<(webrtc_dir)/out/<(configuration)/libaudio_processing.a',
              '<(webrtc_dir)/out/<(configuration)/libaudioproc_debug_proto.a',
              '<(webrtc_dir)/out/<(configuration)/libprotobuf_lite.a',
              '<(webrtc_dir)/out/<(configuration)/libaudio_processing_sse2.a',
              '<(webrtc_dir)/out/<(configuration)/libaudio_device.a',
              '<(webrtc_dir)/out/<(configuration)/librtc_sound.a',
              '<(webrtc_dir)/out/<(configuration)/libfield_trial_default.a',
              '<(webrtc_dir)/out/<(configuration)/libmetrics_default.a',
              '<(webrtc_dir)/out/<(configuration)/librtc_xmllite.a',
              '<(webrtc_dir)/out/<(configuration)/librtc_xmpp.a',
              '<(webrtc_dir)/out/<(configuration)/librtc_p2p.a',
              '<(webrtc_dir)/out/<(configuration)/libusrsctplib.a',
              '<(webrtc_dir)/out/<(configuration)/libvideo_capture_module_internal_impl.a',
              '<(webrtc_dir)/out/<(configuration)/libvideo_render_module_internal_impl.a',
              '<(webrtc_dir)/out/<(configuration)/libjingle_p2p.a',
              '<(webrtc_dir)/out/<(configuration)/libsrtp.a',
#              '<(webrtc_dir)/out/<(configuration)/libsocketrocket.a',
              '-lc++',
              '-framework ApplicationServices',
              '-lm',
              '-framework AudioToolbox',
              '-framework CoreAudio',
              '/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.9.sdk/usr/lib/libicucore.dylib',
            ],
          }
        }],
      ],
    }],
  'conditions': [
    ['OS=="linux" or OS=="android"', {
      'targets': [
        {
          'target_name': 'libpeeracle_so',
          'type': 'shared_library',
          'dependencies': [
            'peeracle',
          ],
          'cflags': [
            '-fPIC'
          ],
          'include_dirs': [
            '<(java_home)/include',
            '<(java_home)/include/linux',
          ],
          'sources': [
            'java/jni/peeracle_jni.cc',
          ],
          'conditions': [
            ['OS=="android"', {
              'variables': {
                # This library uses native JNI exports; tell GYP so that the
                # required symbols will be kept.
                'use_native_jni_exports': 1,
              },
            }],
          ],
        },
        {
          'target_name': 'libpeeracle_jar',
          'type': 'none',
          'actions': [
            {
              'variables': {
                'java_src_dir': 'java/src',
                'build_jar_log': '<(INTERMEDIATE_DIR)/build_jar.log',
                'peeracle_java_files': [
                  'java/src/org/peeracle/DataSource.java',
                  'java/src/org/peeracle/HttpDataSource.java',
                  'java/src/org/peeracle/FileDataSource.java',
                ],
                'android_java_files': [
                ],
              },
              'action_name': 'create_jar',
              'inputs': [
                'build/build_jar.sh',
                '<@(java_files)',
              ],
              'outputs': [
                '<(PRODUCT_DIR)/libpeeracle.jar',
              ],
              'conditions': [
                ['OS=="android"', {
                  'variables': {
                    'java_files': ['<@(peeracle_java_files)', '<@(android_java_files)'],
                    'build_classpath': '<(java_src_dir):<(DEPTH)/third_party/android_tools/sdk/platforms/android-<(android_sdk_version)/android.jar',
                  },
                }, {
                  'variables': {
                    'java_files': ['<@(peeracle_java_files)'],
                    'build_classpath': '<(java_src_dir)',
                  },
                }],
              ],
              'action': [
                'bash', '-ec',
                'mkdir -p <(INTERMEDIATE_DIR) && '
                '{ build/build_jar.sh <(java_home) <@(_outputs) '
                '      <(INTERMEDIATE_DIR)/build_jar.tmp '
                '      <(build_classpath) <@(java_files) '
                '      > <(build_jar_log) 2>&1 || '
                '  { cat <(build_jar_log) ; exit 1; } }'
              ],
            },
          ],
          'dependencies': [
            'libpeeracle_so',
          ],
        },
      ],
    }],
  ],
}
