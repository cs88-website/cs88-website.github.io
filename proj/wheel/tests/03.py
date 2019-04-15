test = {
  'name': 'Problem 3',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from secret import SecretWord
          >>> b = Board(SecretWord("bookkeeper"))
          >>> len(b)
          10
          >>> b.guess('o')
          2
          >>> b
          < _ o o _ _ _ _ _ _ _ : o >
          >>> b.done()
          False
          >>> b.guess('k')
          2
          >>> b
          < _ o o k k _ _ _ _ _ : o,k >
          >>> b.guess('j')
          0
          >>> b
          < _ o o k k _ _ _ _ _ : o,k,j >
          >>> b.word()
          ['_', 'o', 'o', 'k', 'k', '_', '_', '_', '_', '_']
          >>> b.guesses()
          ['o', 'k', 'j']
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from board import Board
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