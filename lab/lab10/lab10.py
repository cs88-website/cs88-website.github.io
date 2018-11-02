# Avoid Key Error

def avoid_keyerror(dictionary, key):
    """ Returns the value associated with key in dictionary. If key 
    does not exist in the dictionary, print out 'Avoid Exception' and
    map it to the string 'no value'.

    >>> d = {1: 'one', 3: 'three', 5: 'five'}
    >>> avoid_keyerror(d, 3)
    'three'
    >>> avoid_keyerror(d, 4)
    Avoid Exception
    >>> d[4]
    'no value'
    """
    "*** YOUR CODE HERE ***"
    


# Safe Sum

def safe_sum(fun, seq, missing=0):
    """Return the sum of fun applied to elements in seq using missing as a replacement
    for those elements on which fun throws an exception

    >>> safe_sum(lambda x: x, [5, "terrible", 4, 3, "two", 1])
    13
    >>> safe_sum(lambda x: 1/x, [1, 2, 0, 3, None, "bad"])
    1.8333333333333333
    """
    def wrap(fun, x, summed):
        "*** YOUR CODE HERE ***"
        

    psum = 0
    for x in seq:
        psum = wrap(fun, x, psum)
    return psum


# Quidditch

class Player:
    def __init__(self, name, base_energy):
        """
        Players have a name, and begin with base_energy.
        """
        self.name = name
        self.base_energy = base_energy

    def energy(self):
        return self.base_energy

class Beater(Player):
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
        

class Chaser(Player):
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
        

class Seeker(Player):
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
        

class Keeper(Player):
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

class Game:
    def __init__(self, players, your_name):
        """
        Sets the game up. players is a list of strings that are names of all 
        of the players. your_name is a string and must be one of the players.
        >>> game = Game(["a", "b", "c", "d", "e", "f"], "a")
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

        if len(Game.werewolves) == 0:
            return True
        elif len(Game.werewolves) > len(Game.villagers):
            return True
        else:
            return False


