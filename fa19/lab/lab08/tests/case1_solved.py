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
          88edf27931981a8f9c94550fae149331
          # locked
          >>> x 
          ac540ef42114afeeb817ac17fe3f58f6
          # locked
          >>> z = list(x) 
          >>> z[0] = 6
          >>> z
          e55c9b07ad1a742f76af59db1026d415
          # locked
          >>> x 
          ac540ef42114afeeb817ac17fe3f58f6
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
