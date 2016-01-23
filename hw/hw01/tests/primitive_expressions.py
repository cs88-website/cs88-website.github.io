test = {
  'name': 'primitive_expressions',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 3
          287ada61eabab45481c038d336cec0d9
          # locked
          >>> 2 + 3
          2a2c5c11d76ef6a196697fa556ae3a0d
          # locked
          >>> -16 - -16
          581086b6b29789659effb7a5da0bfb0f
          # locked
          >>> 3 * 4 + 1
          84d2bcf7974876306bccfc116b6bfc7f
          # locked
          >>> 3 * (4 + 1)
          95957b6860bf3a30b229da4a41866ade
          # locked
          >>> 2 ** 3
          671ed54989b8b2d016a764f4eb59e6f8
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> x = 4
          >>> 3 + x
          92e04b9c9e12e4baa468ce2ece990386
          # locked
          >>> x + y
          dfda46f58105eb6e5be6c5c5ab7b6eb1
          # locked
          >>> x, y = 1, 2
          >>> 3 + x
          f970de4b11828bffd6138ddf36454ecf
          # locked
          >>> x + y
          287ada61eabab45481c038d336cec0d9
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