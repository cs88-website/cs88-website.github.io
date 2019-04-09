test = {
  'name': 'Problem 5',
  'points': 4,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> w = WordMunch("one two, Two. tHree")
          >>> w.words()
          8019ac13d675f2965a069f8b9c3ce2a4
          # locked
          >>> w.frequency()['o']
          acbc69f55aaff18c37a07de1a871122b
          # locked
          >>> key_of_max(w.frequency())
          e352038cc411afa89688b2b0b69d5ca0
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> w = WordMunch("one two, Two. tHree")
          >>> w.words()
          ['one', 'three', 'two']
          >>> w.frequency()['o']
          2
          >>> key_of_max(w.frequency())
          'e'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> c0 = ComputerPlayer(WordSet(['three', 'toooooo', 'ellen']))
          >>> c1 = ComputerPlayer(WordSet(['three', 'toooooo', 'ellen']), 1)
          >>> c2 = ComputerPlayer(WordSet(['three', 'toooooo', 'ellen']), 2)
          >>> b0 = Board(SecretWord('three'))
          >>> b1 = Board(SecretWord('three'))
          >>> b2 = Board(SecretWord('three'))
          >>> c0.guess(b0) # Case 1.1
          439e9b43075bfad8de4c37ae4225e87a
          # locked
          >>> b0.guess(c0.guess(b0)) # Case 1.1
          2076dc9164055f0ee0462680d723a6b5
          # locked
          >>> c0.guess(b0) # Case 1.2
          e352038cc411afa89688b2b0b69d5ca0
          # locked
          >>> b0.guess(c0.guess(b0)) # Case 1.2
          acbc69f55aaff18c37a07de1a871122b
          # locked
          >>> c0.guess(b0) # Case 1.3
          ad3f194f2ad20a35b264e3d07830b210
          # locked
          >>> b0.guess(c0.guess(b0)) # Case 1.3
          2076dc9164055f0ee0462680d723a6b5
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> c0 = ComputerPlayer(WordSet(['three', 'toooooo', 'ellen']))
          >>> c1 = ComputerPlayer(WordSet(['three', 'toooooo', 'ellen']), 1)
          >>> c2 = ComputerPlayer(WordSet(['three', 'toooooo', 'ellen']), 2)
          >>> b0 = Board(SecretWord('three'))
          >>> b1 = Board(SecretWord('three'))
          >>> b2 = Board(SecretWord('three'))
          >>> c1.guess(b1) # Case 2.1
          e352038cc411afa89688b2b0b69d5ca0
          # locked
          >>> b1.guess(c1.guess(b1)) # Case 2.1
          acbc69f55aaff18c37a07de1a871122b
          # locked
          >>> c1.guess(b1) # Case 2.2
          ad3f194f2ad20a35b264e3d07830b210
          # locked
          >>> b1.guess(c1.guess(b1)) # Case 2.2
          2076dc9164055f0ee0462680d723a6b5
          # locked
          >>> c1.guess(b1) # Case 2.3
          6adbf6e6c5d432824aea3c0475f340ea
          # locked
          >>> b1.guess(c1.guess(b1)) # Case 2.3
          5b606ddc0dfd146a851fb63490124567
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> c0 = ComputerPlayer(WordSet(['three', 'toooooo', 'ellen']))
          >>> c1 = ComputerPlayer(WordSet(['three', 'toooooo', 'ellen']), 1)
          >>> c2 = ComputerPlayer(WordSet(['three', 'toooooo', 'ellen']), 2)
          >>> b0 = Board(SecretWord('three'))
          >>> b1 = Board(SecretWord('three'))
          >>> b2 = Board(SecretWord('three'))
          >>> c0.guess(b0) # Case 1.1
          'o'
          >>> b0.guess(c0.guess(b0)) # Case 1.1
          0
          >>> c0.guess(b0) # Case 1.2
          'e'
          >>> b0.guess(c0.guess(b0)) # Case 1.2
          2
          >>> c0.guess(b0) # Case 1.3
          'l'
          >>> b0.guess(c0.guess(b0)) # Case 1.3
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> c0 = ComputerPlayer(WordSet(['three', 'toooooo', 'ellen']))
          >>> c1 = ComputerPlayer(WordSet(['three', 'toooooo', 'ellen']), 1)
          >>> c2 = ComputerPlayer(WordSet(['three', 'toooooo', 'ellen']), 2)
          >>> b0 = Board(SecretWord('three'))
          >>> b1 = Board(SecretWord('three'))
          >>> b2 = Board(SecretWord('three'))
          >>> c1.guess(b1) # Case 2.1
          'e'
          >>> b1.guess(c1.guess(b1)) # Case 2.1
          2
          >>> c1.guess(b1) # Case 2.2
          'l'
          >>> b1.guess(c1.guess(b1)) # Case 2.2
          0
          >>> c1.guess(b1) # Case 2.3
          'h'
          >>> b1.guess(c1.guess(b1)) # Case 2.3
          1
          """,
          'hidden': False,
          'locked': False
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