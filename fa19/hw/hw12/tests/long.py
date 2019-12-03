test = {
  'name': 'long',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM long;
          Princess of the Dawn
          Let There Be Rock
          Overdose
          Livin' On The Edge
          You Oughta Know (Alternate)
          Love, Hate, Love
          Master Of Puppets
          Harvester Of Sorrow
          Wherever I May Roam
          Snoopy's search-Red baron
          Stratus
          Wheels Of Confusion / The Straightener
          Book Of Thel
          Jerusalem
          The Alchemist
          Stone Crazy
          Talkin' 'Bout Women Obviously
          Terra
          Dazed and Confused
          Whole Lotta Love
          I Can't Quit You Baby(2)
          You Shook Me(2)
          How Many More Times
          Advance Romance
          Only A Dream In Rio
          So Tinha De Ser Com Voce
          Sabbra Cadabra
          Turn The Page
          Loverman
          Mercyful Fate
          Astronomy
          Tuesday's Gone
          Innuendo
          River Song
          Living On Love
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
