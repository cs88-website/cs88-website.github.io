test = {
  'name': 'List Slicing',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> x = [1, 2, 3, 4]
          >>> x[1:3]
          d9f2f79c63bb0452cca111f0097f6e01
          # locked
          >>> x[:2]
          85f4791dbde2a41b1fd5129362586cda
          # locked
          >>> x[1:]
          0b59790ac79a2cfefac6e5d199a6af1b
          # locked
          >>> x[-2:3]
          10d6d3f2082a5022fbec819887cd9320
          # locked
          >>> x[-2:4]
          4105fdd22b14e14231ca9721a4f4d0a6
          # locked
          >>> x[0:4:2]
          a2ac037792793d9a90a21125289c4193
          # locked
          >>> x[::-1]
          195dddf24581be91800af2053bec3f39
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}