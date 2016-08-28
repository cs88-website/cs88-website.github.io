test = {
  'name': 'matchmaker',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM matchmaker ORDER BY color LIMIT 50;
          koala|Thinking Out Loud||red
          koala|Thinking Out Loud||blue
          |Sandstorm|#009abf|black and gold
          tiger|Sandstorm|#ff7700|blue
          goat|Sandstorm|4|turquoise
          dog|Sandstorm|black|green
          dog|Sandstorm|black|blue
          dog|Sandstorm|black|green
          dog|Sandstorm|black|orange
          dog|Sandstorm|black|blue
          dog|Sandstorm|black|yellow
          dog|Sandstorm|black|blue
          dog|Sandstorm|black|blue
          dog|Sandstorm|black|green
          dog|Sandstorm|black|red
          panda|Shake It Off|black|black
          cat|That Way|black|navy
          dog|That Way|black|purple
          dog|That Way|black|blue
          dog|That Way|black|purple
          dog|That Way|black|gold
          cat|Hello|black|red
          cat|Hello|black|orange
          dog|Hello|black|blue
          dog|Hello|black|blue
          dog|Thinking Out Loud|black|yellow
          dog|Thinking Out Loud|black|green
          dog|Shake It Off|blue|pink
          dog|Shake It Off|blue|blue
          dog|Shake It Off|blue|blue
          dog|Shake It Off|blue|red
          dog|Shake It Off|blue|orange
          dog|Shake It Off|blue|blue
          dog|Shake It Off|blue|blue
          dog|Shake It Off|blue|blue
          koala|Thinking Out Loud|blue|
          koala|Thinking Out Loud|blue|red
          koala|Thinking Out Loud|blue|blue
          tiger|That Way|blue|blue
          tiger|That Way|blue|green
          tiger|That Way|blue|red
          tiger|Hello|blue|red
          tiger|Hello|blue|blue
          dog|That Way|blue|blue
          dog|That Way|blue|black
          dog|That Way|blue|purple
          dog|That Way|blue|blue
          dog|That Way|blue|purple
          dog|That Way|blue|gold
          panda|Hello|blue|blue
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