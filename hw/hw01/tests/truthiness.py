test = {
  'name': 'Truthiness',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 0 or True
          140baa19d30e3acf70c305fc604a1cc1
          # locked
          >>> not '' or not 0 and False
          140baa19d30e3acf70c305fc604a1cc1
          # locked
          >>> 13 and False
          138f25df9fa384871ec971c4537e4474
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