test = {
  'name': 'parent-height',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite>  select * from by_height;
          herbert
          fillmore
          abraham
          delano
          grover
          barack
          clinton
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read lab11.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
