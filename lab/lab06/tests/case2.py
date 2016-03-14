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
          be63cd44cf224729cfc55922ab561c3d
          # locked
          >>> x
          be63cd44cf224729cfc55922ab561c3d
          # locked
          >>> x = [[0, 'a'],  [1, 'b'], [2, 'c']]
          >>> z = list(x)
          >>> z[0][1] = 'z'
          >>> z
          be63cd44cf224729cfc55922ab561c3d
          # locked
          >>> x
          be63cd44cf224729cfc55922ab561c3d
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