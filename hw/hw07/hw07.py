# Abstractions


full_roster = {
    "Manny Machado" : "Dodgers",
    "Yasiel Puig" : "Dodgers",
    "Aaron Judge" : "Yankees",
    "Clayton Kershaw" : "Dodgers",
    "Giancarlo Stanton" : "Yankees"
}

full_stats = {
    "Manny Machado": ["SO", "1B", "3B", "SO", "HR"],
    "Yasiel Puig": ["3B", "3B", "1B", "1B", "SO"],
    "Aaron Judge": ["SO", "HR", "HR", "1B", "SO"],
    "Clayton Kershaw": ["1B", "SO", "SO", "1B", "SO"],
    "Giancarlo Stanton": ["HR", "SO", "3B", "SO", "2B"],
}

def get_team(player):
    """Returns team that the provided player is a member of.

    >>> get_team("Manny Machado")
    'Dodgers'
    >>> get_team("Aaron Judge")
    'Yankees'
    """
    "*** YOUR CODE HERE ***"
    return ______

def get_stats(player):
    """Returns the statistics associated with the provided player.
    >>> get_stats("Manny Machado")
    ['SO', '1B', '3B', 'SO', 'HR']
    >>> get_stats('Aaron Judge')
    ['SO', 'HR', 'HR', '1B', 'SO']
    """
    "*** YOUR CODE HERE ***"
    return ______



# Dictionaries

def get_players(team):
    """Returns a list of all players who are members of the given team.

    >>> get_players("Dodgers")
    ['Manny Machado', 'Yasiel Puig', 'Clayton Kershaw']
    >>> get_players("Yankees")
    ['Aaron Judge', 'Giancarlo Stanton']
    """
    "*** YOUR CODE HERE ***"
    return _____


def common_players(roster):
    """Returns a dictionary containing values along with a corresponding
    list of keys that had that value from the original dictionary.

    >>> common_players(full_roster)
    {'Dodgers': ['Manny Machado', 'Yasiel Puig', 'Clayton Kershaw'], 'Yankees': ['Aaron Judge', 'Giancarlo Stanton']}
    >>> full_roster = {"bob": "excellent", "barnum": "passing", "beatrice": "satisfactory", "bernice": "passing", "ben": "no pass", "belle": "excellent", "bill": "passing", "bernie": "passing", "baxter": "excellent"}
    >>> common_players(full_roster)
    {'excellent': ['bob', 'belle', 'baxter'], 'passing': ['barnum', 'bernice', 'bill', 'bernie'], 'satisfactory': ['beatrice'], 'no pass': ['ben']}
    """
    "*** YOUR CODE HERE ***"
    return ______


# Back to Abstractions!

# Following Functions have been given to you, do NOT modify

def calculate_batting_average(stats):
    hits = 0
    total_bats = 0
    for at_bat in stats:
        if at_bat != "SO":
            hits += 1
        total_bats += 1
    return float(round(hits/total_bats, 1))

def calculate_slugging_percent(stats):
    bases = 0
    total_bats = 0
    for at_bat in stats:
        if at_bat == "1B":
            bases += 1
        elif at_bat == "2B":
            bases += 2
        elif at_bat == "3B":
            bases += 3
        elif at_bat == "HR":
            bases += 4
        total_bats += 1
    return float(round(bases/total_bats, 1))

# Modify Functions below

def calculate_team_BA(team):
    """Given a single team name, returns the mean batting average of all players on that team. You are encouraged to use previous functions that you've defined already
    >>> calculate_team_BA('Dodgers')
    0.6
    >>> calculate_team_BA('Yankees')
    0.6
    """
    "*** YOUR CODE HERE ***"
    return _____

def calculate_all_team_SP():
    """Returns a dictionary mapping every team to the average slugging percentage of all players on that team. You are encouraged to use previous functions that you've defined already.
    >>> calculate_all_team_SP()
    {'Dodgers': 1.2, 'Yankees': 1.8}
    """
    "*** YOUR CODE HERE ***"
    return _____


