# Election

def make_test_random():
    """A deterministic random function that cycles between
    [0.0, 0.1, 0.2, ..., 0.9] for testing purposes.

    >>> random = make_test_random()
    >>> random()
    0.0
    >>> random()
    0.1
    >>> random2 = make_test_random()
    >>> random2()
    0.0
    """
    rands = [x / 10 for x in range(10)]
    def random():
        rand = rands[0]
        rands.append(rands.pop(0))
        return rand
    return random

random = make_test_random()

### Phase 1: The Player Class
class Player:
    """
    >>> random = make_test_random()
    >>> p1 = Player('Hill')
    >>> p2 = Player('Don')
    >>> p1.popularity
    100
    >>> p1.debate(p2)  # random() should return 0.0
    >>> p1.popularity
    150
    >>> p2.popularity
    100
    >>> p2.votes
    0
    >>> p2.speech(p1)
    >>> p2.votes
    10
    >>> p2.popularity
    110
    >>> p1.popularity
    135

    """
    def __init__(self, name):
        self.name = name
        self.votes = 0
        self.popularity = 100

    def debate(self, other):
        "*** YOUR CODE HERE ***"

    def speech(self, other):
        "*** YOUR CODE HERE ***"

    def choose(self, other):
        return self.speech


### Phase 2: The Game Class
class Game:
    """
    >>> p1, p2 = Player('Hill'), Player('Don')
    >>> g = Game(p1, p2)
    >>> winner = g.play()
    >>> p1 is winner
    True

    """
    def __init__(self, player1, player2):
        self.p1 = player1
        self.p2 = player2
        self.turn = 0

    def play(self):
        while not self.game_over:
            "*** YOUR CODE HERE ***"
        return self.winner

    @property
    def game_over(self):
        return max(self.p1.votes, self.p2.votes) >= 50 or self.turn >= 10

    @property
    def winner(self):
        "*** YOUR CODE HERE ***"


### Phase 3: New Players
class AggressivePlayer(Player):
    """
    >>> random = make_test_random()
    >>> p1, p2 = AggressivePlayer('Don'), Player('Hill')
    >>> g = Game(p1, p2)
    >>> winner = g.play()
    >>> p1 is winner
    True

    """
    def choose(self, other):
        "*** YOUR CODE HERE ***"

class CautiousPlayer(Player):
    """
    >>> random = make_test_random()
    >>> p1, p2 = CautiousPlayer('Hill'), AggressivePlayer('Don')
    >>> p1.popularity = 0
    >>> p1.choose(p2) == p1.debate
    True
    >>> p1.popularity = 1
    >>> p1.choose(p2) == p1.debate
    False

    """
    def choose(self, other):
        "*** YOUR CODE HERE ***"



# Quidditch

class QuidditchPlayer:
    def __init__(self, name, base_energy):
        """
        QuidditchPlayers have a name, and begin with base_energy.
        """
        self.name = name
        self.base_energy = base_energy

    def energy(self):
        return self.base_energy

class Beater(QuidditchPlayer):
    role = "bludgers"

    def energy(self, time):
        """
        Returns the amount of energy left after playing for time minutes. 
        After playing for time minutes, Beaters lose their base energy level 
        divided by the number of minutes. If time is 0, catch the ZeroDivisionError 
        and print "You can't divide by zero!" instead.
        >>> fred = Beater("Fred Weasley", 640)
        >>> fred.energy(40)
        624.0
        >>> fred.energy(0)
        You can't divide by zero!
        """
        "*** YOUR CODE HERE ***"
        

class Chaser(QuidditchPlayer):
    role = "score"
    energy_expended = 20
    
    def __init__(self, name, base_energy, goals):
        """
        Chasers have a name, score goals, and begin with base_energy.
        """
        "*** YOUR CODE HERE ***"
        

    def energy(self, time):
        """
        Returns the amount of energy left after playing for time minutes. For every goal 
        they score, they use energy_expended units of energy. In addition, they also use 
        10% of energy_expended if the number of minutes they have played is a multiple of 9.
        >>> katie = Chaser("Katie Bell", 230, 2)
        >>> katie.energy(20)
        190
        >>> ginny = Chaser("Ginny Weasley", 400, 3)
        >>> ginny.energy(45)
        338.0
        """
        "*** YOUR CODE HERE ***"
        

class Seeker(QuidditchPlayer):
    role = "snitch"
    energy_expended = 5

    def energy(self, time):
        """
        Returns the amount of energy after time minutes. Seekers expend energy_expended 
        units of their energy for every minute they have been playing.
        >>> harry = Seeker("Harry Potter", 700)
        >>> harry.energy(30)
        550
        """
        "*** YOUR CODE HERE ***"
        

class Keeper(QuidditchPlayer):
    role = "guard"
    energy_expended = 50

    def energy(self, time):
        """
        Returns the amount of energy after time minutes. If less than 30 minutes have 
        passed, then Keepers do not lose any energy. If 30 minutes or more have passed, 
        then Keepers expend 80% of their energy_expended units for every full 15 
        minutes that pass.
        >>> oliver = Keeper("Oliver Wood", 380)
        >>> oliver.energy(45)
        260.0
        """
        "*** YOUR CODE HERE ***"
        



# Werewolf

def get_most_common_element(lst):
    return max(set(lst), key=lst.count)

class Pl88yer:
    def __init__(self, name):
        self.name = name
        self.active = True

class Werewolf(Pl88yer):
    def __init__(self, name):
        Pl88yer.__init__(self, name)

    def reveal_player_type(self):
        print("You are a werewolf!")

class Villager(Pl88yer):
    def __init__(self, name):
        Villager.__init__(self, name)    

    def reveal_player_type(self):
        print("You are a villager!")

class WerewolfGame:
    def __init__(self, players, your_name):
        """
        Sets the game up. players is a list of strings that are names of all 
        of the players. your_name is a string and must be one of the players.
        >>> game = WerewolfGame(["a", "b", "c", "d", "e", "f"], "a")
        You are a werewolf!
        >>> game.your_name
        'a'
        >>> game.play("b")
        'Keep playing!'
        >>> len(game.werewolves)
        1
        >>> len(game.villagers)
        4
        >>> game.play("c")
        'Keep playing!'
        >>> game.play("d")
        'Keep playing!'
        >>> game.play("a")
        'Villagers win!'
        >>> game.werewolves
        []
        >>> len(game.villagers)
        2
        """
        if len(players) < 4:
            raise Exception("Not enough players!")
        names = players[0:2]
        self.your_name = your_name
        self.werewolves = [Werewolf(self, w) for w in names]
        self.villagers = [Villager(self, p) for p in players if p not in names]
        self.name_to_player = {}

        for werewolf in self.werewolves:
            self.name_to_player[werewolf.name] = werewolf

        for villager in self.villagers:
            self.name_to_player[villager.name] = villager

        player = self.name_to_player[your_name]
        player.reveal_player_type()

        self.state = "night"

    def play(self, vote):
        """
        While the game is still being played, make a move. vote is the player 
        who you vote for, because you believe they are on the opposing team. 
        You can continue playing until either the villagers or the werewolves win.
        """
        self.make_move(vote)
        if not self.check_if_end_of_game():
            return "Keep playing!"
        else:
            if len(self.werewolves) == 0:
                return "Villagers win!"
            elif len(self.werewolves) > len(self.villagers):
                return "Werewolves win!"

    def make_move(self, vote):
        """
        Every player votes (players arbitrarily vote for themselves). Then, 
        if the state of the game is day, remove the player with the most votes 
        overall, and set the state to night. If the state of the game is night, 
        remove the player with the most votes by werewolves, and set the state to day.
        """
        votes = []
        werewolf_votes = []

        if self.state == "night":
            werewolf_votes.append(vote)
        votes.append(vote)

        for player in self.name_to_player:
            if self.state == "night" and isinstance(player, Werewolf(name)):
                werewolf_votes.append(player)
            votes.append(player)

        if self.state == "day":
            majority_vote = get_most_common_element(votes)
            self.state = "night"
        elif self.state == "night":
            majority_vote = get_most_common_element(werewolf_votes)
            self.state = "day"

        if majority_vote in self.name_to_player:
            self.remove_player(majority_vote)
        else:
            raise Exception("Invalid player.")
        
    def remove_player(player_to_remove):
        """
        Set the player with the majority vote to inactive, and remove it from 
        its respective list of players.
        """
        player = self.name_to_player[player_to_remove]
        self.active = False

        if player in self.werewolves:
            self.werewolves.remove(player)
        elif player in self.villagers:
            self.villagers.remove(player)
        else:
            print("Player already removed!")

    def check_if_end_of_game(self):
        """
        Returns True if the game is over, and False if it is not. The game is over when 
        there are no werewolves remaining, or if there are more werewolves than villagers.
        """

        if len(WerewolfGame.werewolves) == 0:
            return True
        elif len(WerewolfGame.werewolves) > len(WerewolfGame.villagers):
            return True
        else:
            return False


