test = {
  'name': 'tallest',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite>  select * from tallest;
          28|grover
          35|eisenhower
          47|clinton
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read lab08.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}