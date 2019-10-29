test = {
  'name': 'Case 2',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> x = [[0, 'a'],  [1, 'b'], [2, 'c']]
          >>> y = x[:]
          >>> y[0][1] = 'z'
          >>> y
          7d7c7259cfa00301b59e3ce1347c0a4a
          # locked
          >>> x
          7d7c7259cfa00301b59e3ce1347c0a4a
          # locked
          >>> x = [[0, 'a'],  [1, 'b'], [2, 'c']]
          >>> z = list(x)
          >>> z[0][1] = 'z'
          >>> z
          7d7c7259cfa00301b59e3ce1347c0a4a
          # locked
          >>> x
          7d7c7259cfa00301b59e3ce1347c0a4a
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
