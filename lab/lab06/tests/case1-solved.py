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
          93921950c1127d2c8bdf1b64ede9694c
          # locked
          >>> x 
          c86a936f2db9e7444463ae645e3c8b71
          # locked
          >>> z = list(x) 
          >>> z[0] = 6
          >>> z
          a4d507cec14909b14290815d20a23730
          # locked
          >>> x 
          c86a936f2db9e7444463ae645e3c8b71
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