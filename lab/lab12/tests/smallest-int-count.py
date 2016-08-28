test = {
  'name': 'smallest-int-count',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM smallest_int_count LIMIT 50;
          1|190
          2|18
          3|21
          4|7
          5|5
          6|7
          7|7
          8|2
          9|1
          10|3
          11|15
          12|3
          13|6
          14|7
          15|1
          16|1
          17|7
          18|2
          19|6
          21|1
          22|3
          23|9
          24|2
          25|1
          26|7
          27|5
          28|1
          29|1
          31|6
          32|3
          33|1
          34|2
          36|1
          37|5
          39|2
          41|1
          42|2
          43|5
          44|1
          50|1
          53|1
          55|1
          56|1
          57|1
          61|2
          64|1
          67|1
          69|6
          70|1
          71|1
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read lab12_extra.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}