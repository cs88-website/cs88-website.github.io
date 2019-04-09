test = {
  'name': 'Problem 3',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> game = Game(DummyPlayer("pick"), [ DummyPlayer("guess") ] )
          >>> board = game.play(False)
          >>> board.word()
          b5b8c11feaa765c879e7b86f9175a902
          # locked
          >>> len(board.guesses())
          a4f887a75756b32901b543f4e27e2426
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from wordset import Dictionary
      >>> from player import Player, DummyPlayer
      >>> from game import Game
      >>> p = Player("Fred", Dictionary('assets/lincoln.txt'))
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}