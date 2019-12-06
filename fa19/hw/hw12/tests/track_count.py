test = {
  'name': 'track_count',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM track_count;
          1|10
          3|3
          4|8
          5|15
          6|13
          7|12
          9|8
          10|14
          11|12
          12|12
          13|8
          17|10
          19|11
          20|11
          21|18
          24|23
          26|17
          27|14
          29|14
          30|14
          31|9
          33|17
          34|17
          35|11
          36|17
          37|20
          39|21
          40|12
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read hw12.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
