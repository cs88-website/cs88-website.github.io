test = {
  'name': 'pricing',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM pricing LIMIT 20;
          For Those About To Rock (We Salute You)|0.99
          Fast As a Shark|0.99
          Restless and Wild|0.99
          Princess of the Dawn|0.99
          Put The Finger On You|0.99
          Let's Get It Up|0.99
          Inject The Venom|0.99
          Snowballed|0.99
          Evil Walks|0.99
          C.O.D.|0.99
          Breaking The Rules|0.99
          Night Of The Long Knives|0.99
          Spellbound|0.99
          Go Down|0.99
          Dog Eat Dog|0.99
          Let There Be Rock|0.99
          Bad Boy Boogie|0.99
          Problem Child|0.99
          Overdose|0.99
          Hell Ain't A Bad Place To Be|0.99
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
