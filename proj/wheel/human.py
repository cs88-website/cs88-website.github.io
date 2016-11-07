from wordset import Dictionary
from player import Player, ComputerPlayer, HumanPlayer
from game import Game

def human_plays():
    dictionary = Dictionary("assets/lincoln.txt")
    Player(dictionary)
    picker = ComputerPlayer()
    guesser = HumanPlayer("guesser")
    game = Game(picker, [guesser] )
    board =  game.play(True)
    print("Solved ", board.word()," in ",len(board.guesses()), "guesses")

if __name__ == "__main__":
    human_plays()


