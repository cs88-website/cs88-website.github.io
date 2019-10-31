test = {
  'name': 'Case 1',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> x = [1, 2, 3, 4]
          >>> y = x
          >>> y[0] = 5
          >>> y
          42fb4f3fedaad21604e65b19506e621b
          # locked
          >>> x
          42fb4f3fedaad21604e65b19506e621b
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
