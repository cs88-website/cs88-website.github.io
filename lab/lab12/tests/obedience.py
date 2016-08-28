test = {
  'name': 'obedience',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM obedience LIMIT 10;
          7|Image 1
          7|Image 2
          Choose this option instead.|Image 2
          7|Image 5
          Choose this option instead.|Image 5
          7|Image 5
          7|Image 2
          7|Image 4
          I'm a rebel|Image 4
          YOLO!|Image 5
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