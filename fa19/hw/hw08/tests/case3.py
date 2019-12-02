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
          922b31a5aa8a759a99522bba89d2a237
          # locked
          >>> x
          fc645a8a4efa42a1e449a46b4e2955bc
          # locked
          >>> z = x[:]
          >>> z[2][1] = 5
          >>> z
          e448d9aef8d82d431ad95cc5d6805417
          # locked
          >>> x
          e448d9aef8d82d431ad95cc5d6805417
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
