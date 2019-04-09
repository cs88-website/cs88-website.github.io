test = {
  'name': 'Problem 6',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> c0 = ComputerPlayer(WordSet(['three', 'toooooo', 'ellen']))
          >>> c1 = ComputerPlayer(WordSet(['three', 'toooooo', 'ellen']), 1)
          >>> c2 = ComputerPlayer(WordSet(['three', 'toooooo', 'ellen']), 2)
          >>> b0 = Board(SecretWord('three'))
          >>> b1 = Board(SecretWord('three'))
          >>> b2 = Board(SecretWord('three'))
          >>> c2.guess(b2) # Case 3.1
          e352038cc411afa89688b2b0b69d5ca0
          # locked
          >>> b2.guess(c2.guess(b2)) # Case 3.1
          acbc69f55aaff18c37a07de1a871122b
          # locked
          >>> c2.guess(b2) # Case 3.2
          6adbf6e6c5d432824aea3c0475f340ea
          # locked
          >>> b2.guess(c2.guess(b2)) # Case 3.2
          5b606ddc0dfd146a851fb63490124567
          # locked
          >>> c2.guess(b2) # Case 3.3
          90c6d1353f8c170777282506e4b7b253
          # locked
          >>> b2.guess(c2.guess(b2)) # Case 3.3
          5b606ddc0dfd146a851fb63490124567
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from wordset import WordMunch
      >>> from wordset import WordSet
      >>> from board import Board
      >>> from secret import SecretWord
      >>> from utils import key_of_max
      >>> from player import ComputerPlayer
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}