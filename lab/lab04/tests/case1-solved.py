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
          b4ab2c55a5497e47cd7f8f615947dfb0
          # locked
          >>> x 
          47e2f6eb2788aa970511d8cd8a4c5ac6
          # locked
          >>> z = list(x) 
          >>> z[0] = 6
          >>> z
          d8a36d3b270c8c118374caf3a0f63bd4
          # locked
          >>> x 
          47e2f6eb2788aa970511d8cd8a4c5ac6
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