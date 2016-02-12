"""The Game of Cucumber."""

# Cucumber application

#!/usr/bin/env python3

from datascience import Table


##########################################################
# Cards
#  - Cards are represented as a string '<cardval> <suit>'

card_nums = ["2","3", "4", "5", "6", "7", "8", "9", "10","Jack","Queen","King","Ace"]
card_suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

def card_value(card):
    """ Return the value of a card, 2-14, Aces high.
    Cards are strings of the form "<num> <suit>".
    Strings not of this form should return zero

    >>> card_value('2 Clubs')
    2
    >>> card_value('Jack Spades')
    11
    >>> card_value('Ace Diamonds')
    14

    """
    # BEGIN Question 1
    "*** REPLACE THIS LINE ***"
    # END Question 1


##########################################################
# List utilities for hands and players

def remove_item(s, item):
    """Return a list with first occurence of item in sequence removed.

    >>> remove_item([2, 3, 'a', 3], 3)
    [2, 'a', 3]
    >>> remove_item([2, 3, 'a', 3], 2)
    [3, 'a', 3]
    >>> remove_item([2, 3, 'a', 4], 4)
    [2, 3, 'a']
    """

    assert item in s, "Attempt to remove non-existent item from sequence"
    # BEGIN Question 2
    "*** REPLACE THIS LINE ***"
    # END Question 2

def rotate_list(s, n):
    """Return a list containing a sequence rotated left by n elements.

    >>> rotate_list([2, 3, 'a', 4], 0)
    [2, 3, 'a', 4]
    >>> rotate_list([2, 3, 'a', 4], 1)
    [3, 'a', 4, 2]
    >>> rotate_list([2, 3, 'a', 4], 7)
    [4, 2, 3, 'a']
    """
    
    # BEGIN Question 3
    "*** REPLACE THIS LINE ***"
    # END Question 3

##########################################################
# Hands are represented as a list of cards

def new_hand():
    return []

def highest_card(hand):
    """Return the highest value card in a hand.

    >>> highest_card(['Queen Spades', '7 Clubs', 'Ace Spades', '9 Clubs'])
    'Ace Spades'
    """

    assert hand, "Attempt to find highest card of empty hand."
    # BEGIN Question 4
    "*** REPLACE THIS LINE ***"
    # END Question 4

def lowest_card(hand):
    """Return the lowest value card in a hand.

    >>> lowest_card(['Queen Spades', '7 Clubs', 'Ace Spades', '9 Clubs'])
    '7 Clubs'
    """

    # BEGIN Question 4
    "*** REPLACE THIS LINE ***"
    # END Question 4


def playable(hand, value):
    """Return a list of cards in hand with value greater or equal to value

    >>> playable(['Queen Spades', '7 Clubs', 'Queen Clubs', '9 Clubs'], 7)
    ['Queen Spades', '7 Clubs', 'Queen Clubs', '9 Clubs']
    >>> playable(['Queen Spades', '7 Clubs', 'Queen Clubs', '9 Clubs'], 11)
    ['Queen Spades', 'Queen Clubs']
    >>> playable(['Queen Spades', '7 Clubs', 'Queen Clubs', '9 Clubs'], 13)
    []

    """
    # BEGIN Question 6
    "*** REPLACE THIS LINE ***"
    return [] # replace this
    # END Question 6

def legal_play(card, hand, high_value):
    """Determine if card is a legal play for hand.

    >>> legal_play('7 Clubs', ['7 Clubs', '10 Clubs', '2 Hearts'], 7)
    True
    >>> legal_play('7 Clubs', ['7 Clubs', '10 Clubs', '2 Hearts'], 8)
    False
    >>> legal_play('2 Clubs', ['7 Clubs', '10 Clubs', '2 Hearts'], 8)
    False
    >>> legal_play('10 Clubs', ['7 Clubs', '10 Clubs', '2 Hearts'], 8)
    True
    >>> legal_play('3 Clubs', ['7 Clubs', '10 Clubs', '2 Hearts'], 8)
    False
    """
    # BEGIN
    "*** REPLACE THIS LINE ***"
    # END

def print_hands(players, hands):
    """Print the cards held by each player."""
    # You do not need to change this function
    for player, hand in zip(players, hands):
        print(player, "holds", hand)


##########################################################
# Deck of cards
#  - Decks are represented as a Table with one column 'Card'

def new_deck():
    """Return a deck of cards ordered by suit and value within suit.

    >>> new_deck().num_rows
    52
    >>> list(new_deck()["Card"][0:5])
    ['2 Clubs', '3 Clubs', '4 Clubs', '5 Clubs', '6 Clubs']
    >>> list(new_deck()["Card"][46:51])
    ['9 Spades', '10 Spades', 'Jack Spades', 'Queen Spades', 'King Spades']
    """

    # BEGIN Question 7
    "*** REPLACE THIS LINE ***"
    # END Question 7

def shuffle_deck(deck):
    """Return a shuffled deck."""

    # You do not need to change this function
    # It uses Table methods that you have not seen yet
    return deck.sample(deck.num_rows,with_replacement = False)


##########################################################
# Deal from card deck to player's hands

def deal(deck, players, dealer, number_of_cards, shuffle=True):
    """Deal cards to hands associated with each of a list of players.

    deck: a deck of cards
    players: a list of player names
    dealer: index of the dealer in players
    number_of_cards: number of cards to deal to each player from the deck

    Emulate dealing of cards from the deck to each of the hands
    After shuffling the deck, deal the first card to the player to the left
      of the dealer by removing a card from the deck and adding it to the
      player's hand.  Continue until number_of_cards are dealt to each hand

    Return: list of dealt hands

    >>> deal(new_deck(), ["P1", "P2", "P3"],1,3,False)
    [['4 Clubs', '7 Clubs', '10 Clubs'], ['2 Clubs', '5 Clubs', '8 Clubs'], ['3 Clubs', '6 Clubs', '9 Clubs']]

    """
    # BEGIN Question 8
    "*** REPLACE THIS LINE ***"
    return [[] for p in players] # replace this
    # END Question 8

##########################################################
# Board of play
#
#  Board is represented as a table of cards played in a tricks of the round.
#  Rows represent the tricks.
#  'lead' column is the index of the player who leads the trick
#  row is filled in with the cards played by each player as the trick progresses.
#  A player must play a card of value at least as high as the highest 
#  played so far in the round, of their lowest card if they cannot.

def new_board(players):
    """A board is a table containing a record of play in each round.

    >>> new_board(['player0', 'player1', 'player2', 'player3'])
    lead | player0 | player1 | player2 | player3
    """

    # BEGIN Question 9
    "*** REPLACE THIS LINE ***"
    return Table()  # replace this
    # END Question 9

def start_trick(board, lead):
    """Establish the leader in the next trick in a board. Mark all '*NOT PLAYED*'
    

    >>> start_trick(new_board(['player0', 'player1', 'player2', 'player3']),3)
    lead | player0      | player1      | player2      | player3
    3    | *NOT PLAYED* | *NOT PLAYED* | *NOT PLAYED* | *NOT PLAYED*
    """
    # BEGIN Question 10
    "*** REPLACE THIS LINE ***"
    # END Question 10

def play_card(board, player, card):
    """Update board with player playing card.

    >>> b = start_trick(new_board(['p0', 'p1']),0)
    >>> play_card(b, 'p0', '3 Clubs')
    >>> b
    lead | p0      | p1
    0    | 3 Clubs | *NOT PLAYED*
    """
    # BEGIN Question 11
    "*** REPLACE THIS LINE ***"
    # END Question 11

def get_trick(board):
    """Return the index current trick for a board.

    >>> b = new_board(['p0', 'p1'])
    >>> start_trick(b, 1)
    lead | p0           | p1
    1    | *NOT PLAYED* | *NOT PLAYED*
    >>> get_trick(b)
    0
    >>> play_card(b, 'p1', '2 Clubs')
    >>> play_card(b, 'p0', '3 Clubs')
    >>> start_trick(b, 0)
    lead | p0           | p1
    1    | 3 Clubs      | 2 Clubs
    0    | *NOT PLAYED* | *NOT PLAYED*
    >>> get_trick(b)
    1
    >>> play_card(b, 'p0', '4 Clubs')
    >>> get_trick(b)
    1
    >>> b
    lead | p0      | p1
    1    | 3 Clubs | 2 Clubs
    0    | 4 Clubs | *NOT PLAYED*
    """
    # BEGIN Question 12
    "*** REPLACE THIS LINE ***"
    # END Question 12


def get_highest_in_trick(board):
    """Return the value of the highest card play in a trick.

    >>> b = new_board(['p0', 'p1'])
    >>> start_trick(b, 1)
    lead | p0           | p1
    1    | *NOT PLAYED* | *NOT PLAYED*
    >>> get_trick(b)
    0
    >>> play_card(b, 'p1', '2 Clubs')
    >>> get_highest_in_trick(b)
    2
    >>> play_card(b, 'p0', '3 Clubs')
    >>> get_highest_in_trick(b)
    3
    >>> start_trick(b, 0)
    lead | p0           | p1
    1    | 3 Clubs      | 2 Clubs
    0    | *NOT PLAYED* | *NOT PLAYED*
    >>> get_highest_in_trick(b)
    0
    >>> play_card(b, 'p0', '4 Clubs')
    >>> get_highest_in_trick(b)
    4
    """
    # BEGIN Question 13
    "*** REPLACE THIS LINE ***"
    # END Question 13

##########################################################
# Strategy functions
#
# These are some simple strategy functions that can be passed in to
# the game play to assist in testing.
# The manual stategy uses input operations that you haven't seen yet
# You do not need to modify these routines

def play_first(board, player, hand):
    """Play the first playable card in hand."""

    # This is a terrible strategy to get you started
    playable_cards = playable(hand, get_highest_in_trick(board))
    if playable_cards:
        card = playable_cards[0] 
    else:
        card = lowest_card(hand)
    return card


def manual(board, player, hand):
    """Let a real person play the hand."""

    print(player, "current hand", hand)
    print("Current board")
    print(board)
    card = input("Card to play: ")
    while not legal_play(card, hand, get_highest_in_trick(board)):
        print("Sorry.  {0} is not a legal play.".format(card))
        if not (card in hand):
            print("Please enter a card in your hand.")
        else:
            print("Please play as high as previous or lowest in hand.")
        card = input("Card to play: ")
    return card

##########################################################
# Play the game

def play_trick(board, lead, players, hands, strategies):
    """Play a trick and return index of winning player.

    >>> players = ['P0', 'P1']
    >>> hands = deal(new_deck(), players, 0, 3, shuffle=False)
    >>> hands
    [['2 Clubs', '4 Clubs', '6 Clubs'], ['3 Clubs', '5 Clubs', '7 Clubs']]
    >>> board = new_board(players)
    >>> new_lead = play_trick(board, 1, players, hands, [play_first, play_first])
    >>> board
    lead | P0      | P1
    1    | 4 Clubs | 3 Clubs
    >>> hands
    [['2 Clubs', '6 Clubs'], ['5 Clubs', '7 Clubs']]
    >>> play_trick(board, new_lead, players, hands, [play_first, play_first])
    1
    >>> board
    lead | P0      | P1
    1    | 4 Clubs | 3 Clubs
    0    | 2 Clubs | 5 Clubs
    >>> hands
    [['6 Clubs'], ['7 Clubs']]

    """

    # BEGIN Question 14
    "*** REPLACE THIS LINE ***"
    # END Question 14

deck = new_deck()

def play_game(players, strategies, verbose=False, shuffle=True, num_cards=7, dealer=0, max_score=21):
    """
    Play a full game of tricks.

    players: list of player names
    strategies: list containing strategy function for each player

    verbose: print out things that happen in the game (default False)
    shuffle: set to False for testing
    num_cards: number of cards to deal, reduce for testing (default 7)
    dealer: player to deal the cards (default 0)
    max_score: termination point count (reduce for testing)

    returns: list of scores for players
    
    """
    # BEGIN Question 15
    "*** REPLACE THIS LINE ***"
    # END Question 15

def test_game():
    players = ["You", "Bot1", "Bot2", "Bot3"]
    strategies = [manual, play_first, play_first, play_first]
    return play_game(players, strategies, verbose=True, num_cards=3, max_score=11)

##########################################################
# More advanced strategy functions

def lead_second_highest_follow_low(board, player, hand):
    # BEGIN
    "*** REPLACE THIS LINE ***"
    # END

def play(number_of_players=4, verbose=False):
    players = ["player"+str(i) for i in range(number_of_players)]
#    strategies = [manual for player in players]
    strategies = [play_first for player in players]
#    strategies = [lead_second_highest_follow_low for player in players]
    return play_game(players, strategies, verbose)

def main(verbose=False):
    number_of_players=4
    players = ["player"+str(i) for i in range(number_of_players)]
    strategies = [lead_second_highest_follow_low for player in players]
    strategies[0] = manual
    return play_game(players, strategies, verbose)

# if __name__ == '__main__':
#    main(True)




