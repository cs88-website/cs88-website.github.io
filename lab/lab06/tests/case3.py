test = {
  'name': 'Case 3',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> x = [5, 'hello', [1, 1]]
          >>> y = x[:]
          >>> y[0] = 10
          >>> y
          eb83c745c788b11d8b2f79b7a9b1d1b2
          # locked
          >>> x
          0d60954a21987c37cb052aa22a9bdd59
          # locked
          >>> z = x[:]
          >>> z[2][1] = 5
          >>> z
          1387c2bec605e3cff03f59e29dafc72b
          # locked
          >>> x
          1387c2bec605e3cff03f59e29dafc72b
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