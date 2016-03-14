test = {
  'name': 'Case 1',
  'points': 0,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': """
          >>> x = [1, 2, 3, 4]
          >>> y = x
          >>> y[0] = 5
          >>> y
          [5, 2, 3, 4]
          >>> x
          [5, 2, 3, 4] 
          """,
        },
      ]
    }
  ]
}