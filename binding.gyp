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
          'OS!="win"', {
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
