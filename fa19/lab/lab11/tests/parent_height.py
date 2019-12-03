test = {
  'name': 'parent-height',
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
          sqlite>  select * from by_height;
          herbert
          fillmore
          abraham
          delano
          grover
          barack
          clinton
          """,
        },
      ],
    },
  ]
}
