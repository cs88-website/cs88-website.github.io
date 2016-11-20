test = {
  'name': 'small',
  'points': 1,
  'suites': [
    {
      'type': 'sqlite',
      'setup': """
      sqlite> .read lab08.sql
      """,
      'cases': [
        {
          'locked': False,
          'code': r"""
          sqlite> select name from size_of_dogs where size="toy" or size="mini";
          abraham
          eisenhower
          fillmore
          grover
          herbert
          """,
        },
      ],
    },
  ]
}
