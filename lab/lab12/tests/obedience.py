test = {
  'name': 'obedience',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM obedience LIMIT 10;
          7|Option 2
          Choose this option instead.|Option 3
          YOLO!|Option 3
          7|Option 4
          7|Option 5
          YOLO!|Option 3
          Choose this option instead.|Option 3
          Choose this option instead.|Option 3
          7|Option 1
          7|Option 3
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