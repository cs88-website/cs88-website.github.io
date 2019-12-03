test = {
  'name': 'tallest',
  'points': 1,
  'suites': [
    {
      'type': 'sqlite',
      'setup': """
      sqlite> .read lab09.sql
      """,
      'cases': [
        {
          'locked': False,
          'code': r"""
          sqlite>  select * from tallest;
          28|grover
          35|eisenhower
          47|clinton
          """,
        },
      ],
    },
  ]
}
