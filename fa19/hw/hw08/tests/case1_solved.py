test = {
  'name': 'Case 1 Solved',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> x = [1, 2, 3, 4]  
          >>> y = x[:]
          >>> y[0] = 5
          >>> y
          42fb4f3fedaad21604e65b19506e621b
          # locked
          >>> x 
          b2384967e8b6e0f2f37ccd9759f8f47d
          # locked
          >>> z = list(x) 
          >>> z[0] = 6
          >>> z
          89883788a768fba1b2f6455f4ade68c9
          # locked
          >>> x 
          b2384967e8b6e0f2f37ccd9759f8f47d
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
