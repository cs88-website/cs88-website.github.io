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
          1866db478a294cf868da0b5817a30133
          # locked
          >>> x
          1866db478a294cf868da0b5817a30133
          # locked
          >>> x = [[0, 'a'],  [1, 'b'], [2, 'c']]
          >>> z = list(x)
          >>> z[0][1] = 'z'
          >>> z
          1866db478a294cf868da0b5817a30133
          # locked
          >>> x
          1866db478a294cf868da0b5817a30133
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
