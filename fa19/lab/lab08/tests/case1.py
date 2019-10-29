test = {
  'name': 'Case 1',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> x = [1, 2, 3, 4]
          >>> y = x
          >>> y[0] = 5
          >>> y
          88edf27931981a8f9c94550fae149331
          # locked
          >>> x
          88edf27931981a8f9c94550fae149331
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
