test = {
  'name': 'To Boolean or not to Boolean',
  'points': 0,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': """
          >>> ((0 or 5) and (False or '') and 1/0)
          ''
          >>> fi, foo = max, min
          >>> def switcheroo(foo):
          ...     foo = fi
          ...     return 10
          >>> foo(switcheroo(foo), 5)
          5
          """
        }
      ]
    }
  ]
}
