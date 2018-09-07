test = {
  'name': 'Veritasiness',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> True and 13
          84d2bcf7974876306bccfc116b6bfc7f
          # locked
          >>> False or 0
          581086b6b29789659effb7a5da0bfb0f
          # locked
          >>> not 10
          138f25df9fa384871ec971c4537e4474
          # locked
          >>> not None
          140baa19d30e3acf70c305fc604a1cc1
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> True and 1 / 0 and False
          dfda46f58105eb6e5be6c5c5ab7b6eb1
          # locked
          >>> True or 1 / 0 or False
          140baa19d30e3acf70c305fc604a1cc1
          # locked
          >>> True and 0
          581086b6b29789659effb7a5da0bfb0f
          # locked
          >>> False or 1
          feedd0295d99780b4515739c7fc5de8a
          # locked
          >>> 1 and 3 and 6 and 10 and 15
          95957b6860bf3a30b229da4a41866ade
          # locked
          >>> 0 or False or 2 or 1 / 0
          0e848c28f96df07c693ef539595d4380
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