test = {
  'name': 'short',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT name, size FROM short_dogs;
          abraham|26
          eisenhower|35
          fillmore|32
          grover|28
          herbert|31
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