test = {
  'name': 'Pet',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> a = Animal()
          >>> a.is_alive
          8ed0efeabc8e9866128f4f4e97c7ce8e
          # locked
          >>> a.talk()
          65a634faf2a3943a44f4cfc95499fb5e
          # locked
          >>> hamster = Pet("Hamster", 2014)
          >>> hamster.talk()
          671cd9c570be8b9306ee2a5be39b4c4d
          # locked
          >>> hamster.eat("seed")
          671cd9c570be8b9306ee2a5be39b4c4d
          9cdfdc06f17b9c180cece76be6de6d73
          # locked
          >>> hamster.eat("poison")
          65a634faf2a3943a44f4cfc95499fb5e
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}