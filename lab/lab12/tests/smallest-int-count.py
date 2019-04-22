test = {
  'name': 'smallest-int-count',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM smallest_int_count LIMIT 50;
          1|34
          2|4
          3|7
          4|2
          5|1
          6|2
          7|5
          8|1
          10|1
          11|1
          13|1
          14|1
          17|2
          19|2
          31|1
          34|1
          62|1
          99|3
          100|1
          10000000|1
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      sqlite> .read lab12.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
