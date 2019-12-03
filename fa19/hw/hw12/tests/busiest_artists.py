test = {
  'name': 'busiest_artists',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM busiest_artists;
          AC/DC|18
          Accept|3
          Aerosmith|15
          Alanis Morissette|13
          Alice In Chains|12
          Antonio Carlos Jobim|17
          Apocalyptica|8
          Audioslave|26
          BackBeat|12
          Billy Cobham|8
          Black Sabbath|10
          Bruce Dickinson|11
          Buddy Guy|11
          Caetano Veloso|18
          Chico Science & Nacao Zumbi|23
          Cidade Negra|31
          David Coverdale|12
          Frank Zappa & Captain Beefheart|9
          Green Day|21
          Kiss|20
          Led Zeppelin|14
          Marcos Valle|17
          Metallica|11
          Queen|17
          Various Artists|14
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
