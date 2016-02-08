test = {
  'name': 'First',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def foo(x):
          ...     def bar(y):
          ...         return x + y
          ...     return bar
          >>> boom = foo(23)
          >>> boom(42)
          2dc7fead53d98ebfa6c3d610bed1ae6b
          # locked
          >>> foo(6)(7)
          7edad8d629f285ca759c95da679fd452
          # locked
          >>> func = boom
          >>> # "a is b" returns whether a and b are different names for the same thing
          >>> func is boom
          2363e0cf1475978bc3373849c76acf77
          # locked
          >>> func = foo(23)
          >>> func is boom
          30612a20c5efd351c827ed74fa104597
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