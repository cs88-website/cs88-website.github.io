test = {
  'name': 'Truthiness',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 0 or True
          d8c49646e6ef67104d07d32e0792ae6b
          # locked
          >>> not '' or not 0 and False
          d8c49646e6ef67104d07d32e0792ae6b
          # locked
          >>> 13 and False
          af4228e58624c878bd7feab4c248f509
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