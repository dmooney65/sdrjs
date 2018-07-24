{
  "targets": [
    {
      "target_name": "sdrjs",
      "sources": [ "src/sdrjs.cc", "src/device.cc" ],
      "include_dirs": [
        "<!(node -e \"require('nan')\")"
      ],
      "conditions" : [
        [
          'target_arch=="arm"', {
            "libraries" : [
              '<(arm_lib_dir)librtlsdr.so.0'
            ]
          }
        ],
        [
          'OS!="win" and target_arch!="arm"', {
            "libraries" : [
              '-lrtlsdr',
            ],
          }
        ],
        [
          'OS=="win"', {
	          'include_dirs': ['<(rtlsdr_include_dir)'],
            "libraries" : [
              '<(rtlsdr_lib_dir)rtlsdr.lib'
            ]
          }
        ]
      ]
    }
  ]
}
