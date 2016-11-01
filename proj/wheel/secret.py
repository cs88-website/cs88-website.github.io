#
# SecretWord class
#
# Encapsulates a secret word that is provided when an SecretWord object is constructed.
#  The word is kept secret in the interpreter representation and in printing
#  Characteristics of the secret are only visible through
#   - len: returns the number of characters of the secret word.
#   - match: returns a list of the indices of a characters in the secret word
#
class SecretWord:
    """Encapsulate a secret word.

    >>> s = SecretWord('whodoneit')
    >>> len(s)
    9
    >>> s.match('o')
    [2, 4]
    >>> s.match('x')
    []
    >>> s
    <secret word>
    """
    def __init__(self, word):
        """Construct a secret word."""
        # BEGIN Question 1
        "*** REPLACE THIS LINE ***"
        # END Question 1

    def __len__(self):
        """Length of the secret word."""
        # BEGIN
        "*** REPLACE THIS LINE ***"
        # END

    def __repr__(self):
        return "<secret word>"

    def __str__(self):
        return "<secret word>"

    def match(self, char):
        """Return a list of the indices of char in the secret word."""
        # BEGIN Question 1
        "*** REPLACE THIS LINE ***"
        # END Question 1
