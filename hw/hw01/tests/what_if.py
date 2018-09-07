test = {
  'name': 'What If?',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def xk(c, d):
          ...     if c == 4:
          ...         return 6
          ...     elif d >= 4:
          ...         return 6 + 7 + c
          ...     else:
          ...         return 25
          >>> xk(10, 10)
          51f28fccd08d286d5ea13215c5ed8bef
          # locked
          >>> xk(10, 6)
          51f28fccd08d286d5ea13215c5ed8bef
          # locked
          >>> xk(4, 6)
          60daaba01c0f7f95b662d2dee81a75cc
          # locked
          >>> xk(0, 0)
          041cada5cc90e00c9d31f343909921bb
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> def how_big(x):
          ...     if x > 10:
          ...         print('huge')
          ...     elif x > 5:
          ...         return 'big'
          ...     elif x > 0:
          ...         print('small')
          ...     else:
          ...         print("nothin'")
          >>> how_big(7)
          6f824296eb2f8c4f27fc49f3ed2150d5
          # locked
          >>> how_big(12)
          5442808e4bccfea5df364aeec3d11713
          # locked
          >>> how_big(1)
          6336690286e5f79f08c3152b789843b7
          # locked
          >>> how_big(-1)
          9d6db6a3ebbabf49e2a7886c224c7719
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> def so_big(x):
          ...     if x > 10:
          ...         print('huge')
          ...     if x > 5:
          ...         return 'big'
          ...     if x > 0:
          ...         print('small')
          ...     print("nothin'")
          >>> so_big(7)
          6f824296eb2f8c4f27fc49f3ed2150d5
          # locked
          >>> so_big(12)
          5442808e4bccfea5df364aeec3d11713
          6f824296eb2f8c4f27fc49f3ed2150d5
          # locked
          >>> so_big(1)
          6336690286e5f79f08c3152b789843b7
          9d6db6a3ebbabf49e2a7886c224c7719
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