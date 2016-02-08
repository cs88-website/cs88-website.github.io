test = {
  'name': 'Square',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def square(x):
          ...     return x * x
          53cf1f506826c54971339dcc19807024
          # locked
          >>> def neg(f, x):
          ...     return -f(x)
          53cf1f506826c54971339dcc19807024
          # locked
          >>> neg(square, 4)
          16b16382e565d37cf26464067a3e8375
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