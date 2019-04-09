test = {
  'name': 'Problem 4',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> p.possible_words[2]
          'add'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> game = Game(DummyPlayer("pick"), [ DummyPlayer("guess") ] )
          >>> board = game.play(False)
          >>> board.word()
          ['s', 'c', 'o', 'r', 'e']
          >>> len(board.guesses())
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> c = ComputerPlayer()
          >>> c.pick_word()
          'dead'
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from Wordset import Dictionary
      >>> from player import Player, DummyPlayer, ComputerPlayer
      >>> from game import Game
      >>> p = Player("Fred", Dictionary('assets/lincoln.txt'))
      >>> import random
      >>> random.seed(42)
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}