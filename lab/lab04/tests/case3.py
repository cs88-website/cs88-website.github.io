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
          bf1473a72327d5615678ae87dba68c05
          # locked
          >>> x
          43fd10e3a8899a6f099c7acd82a8a558
          # locked
          >>> z = x[:]
          >>> z[2][1] = 5
          >>> z
          a0b74701d942b84aa090d3cfbf279731
          # locked
          >>> x
          a0b74701d942b84aa090d3cfbf279731
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