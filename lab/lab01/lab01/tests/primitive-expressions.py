test = {
  'name': 'primitive-expressions',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 3
          95e06bb41a8511e42188cb3fde2ddb68
          # locked
          >>> 2 + 3
          45d2cef3b717b1b5edc7f57ec2e831f0
          # locked
          >>> -16 - -16
          b0754f6baafe74512d1be0bd5c8098ed
          # locked
          >>> 3 * 4 + 1
          72c74b6c7ed80d51f9fa7defbf7ed121
          # locked
          >>> 3 * (4 + 1)
          438f344a520081fe8e2d0da944a5240b
          # locked
          >>> 2 ** 3
          44b009a8ae29e806844d66237881d263
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> x = 4
          >>> 3 + x
          f3f0d7ed9a5f7790e7d6be65f44e207a
          # locked
          >>> x + y
          d7b5fd49f83e4ee318af207fc969c9f4
          # locked
          >>> x, y = 1, 2
          >>> 3 + x
          9f3942462dcdc25005b450dc0da0adb5
          # locked
          >>> x + y
          95e06bb41a8511e42188cb3fde2ddb68
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