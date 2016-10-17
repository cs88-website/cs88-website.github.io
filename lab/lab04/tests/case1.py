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
          b4ab2c55a5497e47cd7f8f615947dfb0
          # locked
          >>> x
          b4ab2c55a5497e47cd7f8f615947dfb0
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