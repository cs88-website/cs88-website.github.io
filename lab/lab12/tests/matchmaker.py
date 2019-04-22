test = {
  'name': 'matchmaker',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM matchmaker ORDER BY color LIMIT 50;
          dog|"I Want it That Way"" by Backstreet Boys|none|blue
          dog|"I Want it That Way"" by Backstreet Boys|none|blue
          dog|"Hello" by Adele|green|pink
          dog|"Hello" by Adele|green|purple
          dog|"I Want it That Way"" by Backstreet Boys|blue|blue
          dog|"Thinking Out Loud" by Ed Sheeran|don't have one|black
          dog|"Thinking Out Loud" by Ed Sheeran|don't have one|black
          owl|"Hello" by Adele|blue|blue
          dog|"Hello" by Adele|pink|purple
          dolphin|"I Want it That Way"" by Backstreet Boys|green|blue
          cat|"Hello" by Adele|pink|blue
          dog|"Hotline Bling" by Drake|white|blue
          dog|"Hotline Bling" by Drake|white|black
          dog|"Thinking Out Loud" by Ed Sheeran|black|black
          dog|"Hotline Bling" by Drake|blue|black
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