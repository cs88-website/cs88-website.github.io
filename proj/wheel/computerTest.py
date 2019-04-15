from wordset import Dictionary
from player import Player, ComputerPlayer, HumanPlayer
from game import Game

def play_and_add(picker, guesser, d, verbose):
    """
    Runs a game with the picker and guesser and adds
    the word guessed in that game to the dictionary d.
    HINT: Use add_board_result_to_d :)
    HINT: See computer.py for an example of how to run a game.
    """
    # BEGIN
    "*** YOUR CODE HERE ***"
    # END

def add_board_result_to_d(board, d):
    """
    Adds the word guessed on the board to the dictionary d.
    """
    assert board.done(), "Only add completed words to dictionary"
    d["".join(board.word())] = len(board.guesses())

def d_contained_in(d1, d2):
    assert d1 != {}, "D1 cannot be empty"
    for i in d1:
        assert d1[i] <= d2[i], "Mismatched value for key {} v1:{} v2:{}".format(str(i), d1[i], d2[i])

def computer_plays(a, b, verbose=False):
    """
    Runs computer guessers on the words in the range(a,b) in the Gettysburg
    address dictionary. This dictionary is what is used by default when creating
    a computer player. Return three dictionaries mapping words to the number of
    guesses your player took where g0 corresponds to your dictionary for skill
    level 0, g1 --> skill level 1, g2 --> skill level 2. Start by implementing
    `play_and_add`. After that the provided code will populate g0 correctly. Using
    that as an example. fill in g1 and g2 to complete the test. The doctest below
    compares your g0, g1, g2 to the staffs solution. If you match or beat our
    guess rate, you will pass the test:)

    >>> g0, g1, g2 = computer_plays(0, 100)
    >>> d_contained_in(g0, staff_g0)
    >>> d_contained_in(g1, staff_g1)
    >>> d_contained_in(g2, staff_g2) # Should not pass until after q6
    """
    picker = ComputerPlayer(name="you")
    g0 = {}
    g1 = {}
    g2 = {}
    for i in range(a, b):
        # Changes the pick_word method, so we deterministically get the words in (a, b)
        picker.pick_word = lambda : picker.possible_words.words()[i]
        # A skill level 0 guesser with the Gettysburg address dictionary
        guesser0 = ComputerPlayer(name="AI thing")
        play_and_add(picker, guesser0, g0, verbose)
        # BEGIN
        "*** YOUR CODE HERE ***"
        # END
    # # Might be useful in debugging
    # print("Guesser skill level 0: ", g0)
    # print("Guesser skill level 1: ", g1)
    # print("Guesser skill level 2: ", g2)
    return g0, g1, g2

if __name__ == "__main__":
    picker = ComputerPlayer(name="you")
    computer_plays(0, len(picker.possible_words.words()))

"""
Dictionary mapping words to number of guesses for the staffs version of each
computer player skill_level. g0 corresponds to level 0, g1 to 1, g2 to 2.
Use this to test if your guesser matches the staff solution!
Try to see if you can automate this testing:)
"""
staff_g0 = {'a': 5, 'above': 18, 'add': 8, 'advanced': 16, 'ago': 12, 'all': 9, 'altogether': 12, 'and': 8, 'any': 21, 'are': 5, 'as': 11, 'battlefield': 18, 'be': 18, 'before': 18, 'birth': 18, 'brave': 18, 'brought': 18, 'but': 18, 'by': 21, 'can': 13, 'cause': 15, 'civil': 16, 'come': 19, 'conceived': 16, 'consecrate': 13, 'consecrated': 13, 'continent': 13, 'created': 13, 'dead': 8, 'dedicate': 13, 'dedicated': 13, 'detract': 13, 'devotion': 16, 'did': 8, 'died': 8, 'do': 8, 'earth': 10, 'endure': 15, 'engaged': 12, 'equal': 23, 'far': 14, 'fathers': 14, 'field': 14, 'final': 14, 'fitting': 14, 'for': 14, 'forget': 14, 'forth': 14, 'fought': 15, 'four': 15, 'freedom': 19, 'from': 19, 'full': 15, 'gave': 16, 'god': 12, 'government': 19, 'great': 12, 'ground': 15, 'hallow': 17, 'have': 16, 'here': 10, 'highly': 21, 'honored': 10, 'in': 7, 'increased': 13, 'is': 11, 'it': 7, 'larger': 12, 'last': 11, 'liberty': 21, 'little': 9, 'live': 16, 'lives': 16, 'living': 16, 'long': 12, 'measure': 19, 'men': 19, 'met': 19, 'might': 19, 'nation': 7, 'never': 16, 'new': 17, 'nobly': 21, 'nor': 6, 'not': 6, 'note': 6, 'now': 17, 'of': 14, 'on': 6, 'or': 4, 'our': 15, 'people': 20, 'perish': 20, 'place': 20, 'poor': 20, 'portion': 20, 'power': 20, 'proper': 20, 'proposition': 20, 'rather': 10, 'remaining': 19, 'remember': 19, 'resolve': 16, 'resting': 12, 'say': 21, 'score': 13, 'sense': 11, 'seven': 16, 'shall': 11, 'should': 15, 'so': 11, 'struggled': 15, 'take': 22, 'task': 22, 'testing': 12, 'that': 10, 'the': 10, 'their': 10, 'these': 11, 'they': 21, 'this': 11, 'those': 11, 'thus': 15, 'to': 4, 'under': 15, 'unfinished': 15, 'us': 15, 'vain': 16, 'war': 17, 'we': 17, 'what': 17, 'whether': 17, 'which': 17, 'who': 17, 'will': 17, 'work': 22, 'world': 17, 'years': 21}

staff_g1 = {'a': 1, 'above': 13, 'add': 4, 'advanced': 11, 'ago': 10, 'all': 12, 'altogether': 14, 'and': 4, 'any': 15, 'are': 6, 'as': 8, 'battlefield': 14, 'be': 5, 'before': 16, 'birth': 13, 'brave': 13, 'brought': 17, 'but': 16, 'by': 14, 'can': 17, 'cause': 16, 'civil': 12, 'come': 19, 'conceived': 15, 'consecrate': 11, 'consecrated': 12, 'continent': 10, 'created': 14, 'dead': 9, 'dedicate': 10, 'dedicated': 7, 'detract': 14, 'devotion': 11, 'did': 18, 'died': 9, 'do': 9, 'earth': 8, 'endure': 13, 'engaged': 9, 'equal': 22, 'far': 9, 'fathers': 12, 'field': 15, 'final': 15, 'fitting': 12, 'for': 9, 'forget': 14, 'forth': 15, 'fought': 14, 'four': 15, 'freedom': 16, 'from': 18, 'full': 15, 'gave': 17, 'god': 10, 'government': 17, 'great': 18, 'ground': 13, 'hallow': 18, 'have': 11, 'here': 8, 'highly': 19, 'honored': 10, 'in': 6, 'increased': 11, 'is': 3, 'it': 7, 'larger': 11, 'last': 10, 'liberty': 21, 'little': 8, 'live': 11, 'lives': 11, 'living': 17, 'long': 17, 'measure': 17, 'men': 13, 'met': 13, 'might': 21, 'nation': 11, 'never': 11, 'new': 8, 'nobly': 20, 'nor': 5, 'not': 7, 'note': 14, 'now': 8, 'of': 10, 'on': 6, 'or': 11, 'our': 14, 'people': 10, 'perish': 15, 'place': 19, 'poor': 20, 'portion': 18, 'power': 19, 'proper': 10, 'proposition': 12, 'rather': 11, 'remaining': 13, 'remember': 12, 'resolve': 19, 'resting': 11, 'say': 19, 'score': 12, 'sense': 10, 'seven': 11, 'shall': 6, 'should': 15, 'so': 2, 'struggled': 14, 'take': 13, 'task': 13, 'testing': 11, 'that': 5, 'the': 11, 'their': 8, 'these': 8, 'they': 21, 'this': 10, 'those': 9, 'thus': 15, 'to': 7, 'under': 16, 'unfinished': 16, 'us': 12, 'vain': 14, 'war': 8, 'we': 13, 'what': 16, 'whether': 20, 'which': 17, 'who': 11, 'will': 16, 'work': 16, 'world': 17, 'years': 20}

staff_g2 = {'a': 1, 'above': 6, 'add': 2, 'advanced': 6, 'ago': 7, 'all': 3, 'altogether': 8, 'and': 3, 'any': 5, 'are': 6, 'as': 3, 'battlefield': 8, 'be': 5, 'before': 5, 'birth': 7, 'brave': 6, 'brought': 8, 'but': 9, 'by': 6, 'can': 4, 'cause': 7, 'civil': 8, 'come': 7, 'conceived': 7, 'consecrate': 8, 'consecrated': 9, 'continent': 6, 'created': 7, 'dead': 3, 'dedicate': 6, 'dedicated': 6, 'detract': 6, 'devotion': 7, 'did': 5, 'died': 3, 'do': 2, 'earth': 5, 'endure': 5, 'engaged': 5, 'equal': 5, 'far': 3, 'fathers': 7, 'field': 7, 'final': 7, 'fitting': 6, 'for': 5, 'forget': 7, 'forth': 8, 'fought': 9, 'four': 7, 'freedom': 6, 'from': 7, 'full': 8, 'gave': 4, 'god': 6, 'government': 8, 'great': 5, 'ground': 8, 'hallow': 7, 'have': 5, 'here': 3, 'highly': 7, 'honored': 8, 'in': 4, 'increased': 8, 'is': 4, 'it': 5, 'larger': 5, 'last': 5, 'liberty': 7, 'little': 4, 'live': 7, 'lives': 7, 'living': 7, 'long': 8, 'measure': 6, 'men': 5, 'met': 8, 'might': 8, 'nation': 8, 'never': 4, 'new': 5, 'nobly': 10, 'nor': 4, 'not': 5, 'note': 9, 'now': 6, 'of': 2, 'on': 3, 'or': 4, 'our': 5, 'people': 4, 'perish': 6, 'place': 7, 'poor': 6, 'portion': 7, 'power': 7, 'proper': 4, 'proposition': 8, 'rather': 5, 'remaining': 8, 'remember': 4, 'resolve': 6, 'resting': 7, 'say': 7, 'score': 5, 'sense': 3, 'seven': 4, 'shall': 6, 'should': 8, 'so': 3, 'struggled': 11, 'take': 7, 'task': 6, 'testing': 6, 'that': 4, 'the': 8, 'their': 5, 'these': 4, 'they': 5, 'this': 5, 'those': 5, 'thus': 6, 'to': 4, 'under': 5, 'unfinished': 8, 'us': 5, 'vain': 6, 'war': 4, 'we': 6, 'what': 5, 'whether': 5, 'which': 7, 'who': 6, 'will': 9, 'work': 7, 'world': 8, 'years': 5}
