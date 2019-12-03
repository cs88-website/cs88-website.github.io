test = {
  'name': 'long_album',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM long_album;
          Restless and Wild
          Let There Be Rock
          Let There Be Rock
          Big Ones
          Jagged Little Pill
          Facelift
          Plays Metallica By Four Cellos
          Plays Metallica By Four Cellos
          Plays Metallica By Four Cellos
          The Best Of Billy Cobham
          The Best Of Billy Cobham
          Black Sabbath Vol. 4 (Remaster)
          Chemical Wedding
          Chemical Wedding
          Chemical Wedding
          The Best Of Buddy Guy - The Millenium Collection
          The Best Of Buddy Guy - The Millenium Collection
          Prenda Minha
          BBC Sessions [Disc 1] [Live]
          BBC Sessions [Disc 1] [Live]
          BBC Sessions [Disc 1] [Live]
          BBC Sessions [Disc 1] [Live]
          BBC Sessions [Disc 1] [Live]
          Bongo Fury
          Chill: Brazil (Disc 2)
          Chill: Brazil (Disc 2)
          Garage Inc. (Disc 1)
          Garage Inc. (Disc 1)
          Garage Inc. (Disc 1)
          Garage Inc. (Disc 1)
          Garage Inc. (Disc 1)
          Garage Inc. (Disc 1)
          Greatest Hits II
          Into The Light
          Into The Light
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
