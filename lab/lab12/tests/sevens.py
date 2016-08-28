test = {
  'name': 'sevens',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM sevens;
          7
          7
          7
          Choose this option instead.
          I do what I want.
          Choose this option instead.
          7
          YOLO!
          You are not the boss of me!
          Choose this option instead.
          7
          Choose this option instead.
          You are not the boss of me!
          7
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read lab12.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}