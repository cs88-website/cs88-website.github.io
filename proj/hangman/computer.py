from wordset import Dictionary
from player import Player, ComputerPlayer, HumanPlayer
from game import Game

def computer_plays():
    dictionary = Dictionary("assets/lincoln.txt")
    Player(dictionary)
    picker = HumanPlayer("you")
    guesser = ComputerPlayer("AI thing")
    game = Game(picker, [guesser] )
    board =  game.play(True)
    print("Solved ", board.word()," in ",len(board.guesses()), "guesses")

if __name__ == "__main__":
    computer_plays()
