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
          312591917324c5d26a2449f4a7e9ee8c
          # locked
          >>> x
          312591917324c5d26a2449f4a7e9ee8c
          # locked
          >>> x = [[0, 'a'],  [1, 'b'], [2, 'c']]
          >>> z = list(x)
          >>> z[0][1] = 'z'
          >>> z
          312591917324c5d26a2449f4a7e9ee8c
          # locked
          >>> x
          312591917324c5d26a2449f4a7e9ee8c
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