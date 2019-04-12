from wordset import Dictionary
from player import Player, ComputerPlayer, HumanPlayer
from game import Game

def computer_plays():
    picker = HumanPlayer(name="you")
    guesser = ComputerPlayer(name="AI thing")
    game = Game(picker, [guesser] )
    board =  game.play(True)
    print("Solved ", board.word()," in ",len(board.guesses()), "guesses")

if __name__ == "__main__":
    computer_plays()
