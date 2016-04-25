test = {
  'name': 'HOF',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def first(x):
          ...     x += 8
          ...     def second(y):
          ...         print('second')
          ...         return x + y
          ...     print('first')
          ...     return second
          >>> f = first(15)
          0cd62462fa747373868997245aecd4b2
          # locked
          >>> f
          4f02258d689b15b516174b381ad2aef8
          # locked
          >>> f(16)
          eb79794267854191554e088876646a17
          45daa0af063be1f2e19d22b17c5d51ed
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> def even(f):
          ...     def odd(x):
          ...         if x < 0:
          ...             return f(-x)
          ...         return f(x)
          ...     return odd
          >>> stevphen = lambda x: x
          >>> stewart = even(stevphen)
          >>> stewart
          4f02258d689b15b516174b381ad2aef8
          # locked
          >>> stewart(61)
          fca276f013f718468273f07db52f3ab7
          # locked
          >>> stewart(-4)
          ef6b0e7c554b5515158e88d1ee908645
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