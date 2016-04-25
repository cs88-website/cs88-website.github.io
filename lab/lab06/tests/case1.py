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
          93921950c1127d2c8bdf1b64ede9694c
          # locked
          >>> x
          93921950c1127d2c8bdf1b64ede9694c
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