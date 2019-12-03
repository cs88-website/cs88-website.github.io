test = {
  'name': 'short',
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
          sqlite> SELECT name, size FROM short_dogs;
          abraham|26
          eisenhower|35
          fillmore|32
          grover|28
          herbert|31
          """,
        },
      ],
    },
  ]
}
