test = {
  'name': 'Case 3',
  'points': 0,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': """
          >>> x = [5, 'hello', [1, 1]]
          >>> y = x[:]
          >>> y[0] = 10
          >>> y
          [10, 'hello', [1, 1]]
          >>> x
          [5, 'hello', [1, 1]]
          >>> z = x[:]
          >>> z[2][1] = 5
          >>> z
          [5, 'hello', [1, 5]]
          >>> x
          [5, 'hello', [1, 5]] 
          """,
        },
      ]
    }
  ]
}