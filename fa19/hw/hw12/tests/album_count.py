test = {
  'name': 'album_count',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM album_count LIMIT 30;
          AC/DC|2
          Aaron Copland & London Symphony Orchestra|1
          Aaron Goldberg|1
          Academy of St. Martin in the Fields & Sir Neville Marriner|1
          Academy of St. Martin in the Fields Chamber Ensemble & Sir Neville Marriner|1
          Academy of St. Martin in the Fields, John Birch, Sir Neville Marriner & Sylvia McNair|1
          Academy of St. Martin in the Fields, Sir Neville Marriner & Thurston Dart|1
          Accept|2
          Adrian Leaper & Doreen de Feis|1
          Aerosmith|1
          Aisha Duo|1
          Alanis Morissette|1
          Alberto Turco & Nova Schola Gregoriana|1
          Alice In Chains|1
          Amy Winehouse|2
          Anne-Sophie Mutter, Herbert Von Karajan & Wiener Philharmoniker|1
          Antal Dorati & London Symphony Orchestra|1
          Antonio Carlos Jobim|2
          Apocalyptica|1
          Aquaman|1
          Audioslave|3
          BackBeat|1
          Barry Wordsworth & BBC Concert Orchestra|1
          Battlestar Galactica|2
          Battlestar Galactica (Classic)|1
          Berliner Philharmoniker & Hans Rosbaud|1
          Berliner Philharmoniker & Herbert Von Karajan|3
          Berliner Philharmoniker, Claudio Abbado & Sabine Meyer|1
          Billy Cobham|1
          Black Label Society|2
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
