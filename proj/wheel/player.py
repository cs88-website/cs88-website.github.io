"""Player classes for Wheel of Fortune game."""

from wordset import WordMunch
from utils import *
import random

class Player:
    """Player base class.  Defines initializer and interface.

    >>> from wordset import Dictionary
    >>> p = Player(Dictionary('assets/lincoln.txt'))
    >>> Player.all_words[2]
    'add'
    """
    all_words = None

    def __init__(self, dictionary):
        """Inialize class with a dictionary."""
        # BEGIN
        "*** REPLACE THIS LINE ***"
        # END

    def guess(self, board):
        """Return a character a a guess."""
        return None

    def pick_word(self):
        """Return a word that is to be guessed."""
        return None

class DummyPlayer(Player):
    """Simple deterministic player for testing."""

    def __init__(self, name):
        self.name = name
        self.calls = -1

    def guess(self, board):
        """Return a character a a guess."""
        self.calls += 1
        return "cfeors"[self.calls]

    def pick_word(self):
        """Return a word that is to be guessed."""
        return 'score'


class HumanPlayer(Player):
    """HumanPlayer is initialized with a name and implements the player interface
    such that:
    - guess requests a guess from a person, via the input device
    - pick_word requests a secret word and verifies that it is in the dictionary

    """
    def __init__(self, name):
        self.name = name

    def guess(self, board):
        """Guess a character."""

        print(self.name, ", please enter your next guess.")
        guess = input()
        while (len(guess) != 1) or (guess in board.guesses()):
            print('Please enter a single character not yet guessed')
            guess = input()
        return guess

    def pick_word(self):
        """Return a secret word from the dictionary."""

        print(self.name,", pick your secret word.")
        word = input()
        while not word in Player.all_words:
            print(word, " is not in the dictionary. Another:")
            word = input()
        return word

class ComputerPlayer(Player):
    """Perform as a player - picking a word or guessing a character

    >>> from wordset import WordSet    # Basic test including total character frequency
    >>> from board import Board
    >>> from secret import SecretWord
    >>> p = Player(WordSet(['one','two','three']))   # Player superclass with the dictionary
    >>> c = ComputerPlayer()
    >>> b = Board(SecretWord('three'))
    >>> c.guess(b)
    'e'
    """
    def __init__(self, name='Computer'):
        # BEGIN
        "*** REPLACE THIS LINE ***"
        # END

    def guess(self, board, verbose=False):
        """Guess a character to play based on the current board.
        verbose option allows useful and fun displays.
        """
        # BEGIN
        "*** REPLACE THIS LINE ***"
        # END

    def pick_word(self):
        """Pick a random word from the dictionary."""
        # BEGIN
        "*** REPLACE THIS LINE ***"
        # END
