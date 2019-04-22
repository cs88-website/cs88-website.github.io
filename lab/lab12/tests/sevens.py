test = {
  'name': 'sevens',
  'points': 0,
  'suites': [
    {
      'type': 'sqlite',
      'setup': """
      sqlite> .read lab12.sql
      """,
      'cases': [
        {
          'locked': False,
          'code': r"""
          sqlite> SELECT * FROM sevens;
          7
          """,
        },
      ],
    },
  ]
}
