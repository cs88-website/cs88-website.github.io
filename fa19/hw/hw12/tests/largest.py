test = {
  'name': 'largest',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM largest;
          How Many More Times|711836
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read hw12.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
