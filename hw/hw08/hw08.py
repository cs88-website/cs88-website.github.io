## Review on Dictionary

def merge_dict(d1, d2):
    """Returns a dictionary with two dictionaries merged together. You can assume that the same keys appear in both dictionaries. 

    >>> cs61a = {"midterms":2, "projects":3}
    >>> cs61b = {"midterms":2, "projects":4}
    >>> combined = merge_dict(cs61a, cs61b)
    >>> combined
    {'midterms': 4, 'projects': 7}
    """
    "*** YOUR CODE HERE ***"
    return ______

# Mutation

def merge_dict_mutate(d1, d2):
    """Write a function that merge the second dictionary into the first dictionary. You can assume 
    that the same keys appear in both dictionaries. 

    >>> bank = {"Annie":1000, "David":500}
    >>> new_deposits = {"Annie":700, "David":800}
    >>> merge_dict_mutate(bank, new_deposits)
    >>> bank
    {'Annie': 1700, 'David': 1300}
    """
    "*** YOUR CODE HERE ***"
    "SOLUTION HERE"

def list_combine(lst):
    """Write a function that combines all the items in the list into one item and put it as the only item in the list. 

    >>> pokemon = [4, 5, 3, 2, 1, 6]
    >>> list_combine(pokemon)
    >>> pokemon
    [21]
    >>> alphabet = ["a", "b", "c", "d", "e"]
    >>> list_combine(alphabet)
    >>> alphabet
    ['abcde']
    """
    "*** YOUR CODE HERE ***"
    

def dict_cycle(dictionary):
    """Write a function that cycles each of the key-value pair such that the key becomes the last
        item in the value list, and the first item of the list becomes the new key. 

    >>> hamster = {"a":["b","c","d"], "w":["x","y","z"]}
    >>> dict_cycle(hamster)
    >>> hamster
    {'b': ['c', 'd', 'a'], 'x': ['y', 'z', 'w']}
    """
    "*** YOUR CODE HERE ***"
    

def make_gym(a, b, c, d):
    """Returns a pokemon gym (represented by list) of the four pokemons a, b, c, d."""
    return [a, b, c, d]

def gym_size(gym):
    """Returns the size of the gym."""
    return len(gym)

def make_pokemon_set():
    """Returns a dictionary of pokemon methods.

    >>> my_pokemons = make_pokemon_set()
    >>> my_pokemons["add"]("pikachu", "raichu")
    >>> my_pokemons["evolve"]("charmander")
    'charizard'
    >>> my_pokemons["evolve"]("celebi")
    'celebi'
    >>> my_gym = make_gym("charmander", "celebi", "pikachu", "rattata")
    >>> my_pokemons["evolve_all"](my_gym)
    >>> my_gym
    ['charizard', 'celebi', 'pikachu', 'raticate']

    """
    
    pokemons = {"charmander":"charmeleon",
            "charmeleon":"charizard",
            "squirtle":"wartortle",
            "wartortle":"blastoise",
            "rattata":"raticate",
            "sandshrew":"sandslash"}

    def add(pokemon, evolution):
        "*** YOUR CODE HERE ***"
        

    def evolve(pokemon):
        "*** YOUR CODE HERE ***"
        return "SOLUTION HERE"

    def evolve_all(gym):
        "*** YOUR CODE HERE ***"
        

    return {"add":add, "evolve":evolve, "evolve_all":evolve_all}

def _add_pokemon(pokemon_set, pokemon, evolution):
    """Takes in a pokemon and the form it evolves to and adds it to the pokemon
    dictionary set. 
    """
    "*** YOUR CODE HERE ***"
    

def _evolve(pokemon_set, pokemon):
    """Takes in a pokemon and returns its final evolved form. Use the pokemon_set to check for 
    what the pokemon should evolve to. If the pokemon is not in the pokemon set, keeps its 
    status as is. 

    """
    "*** YOUR CODE HERE ***"
    

def _evolve_all(pokemon_set, gym):
    """Takes in a gym and evolve all the pokemons in the gym. You should be modifying the gym,
    not returning a new gym. Use the evolve function you've defined above!

    """
    "*** YOUR CODE HERE ***"
    

