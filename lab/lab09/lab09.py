# Warmup
class Cat(Pet):
    """
    >>> my_cat = Cat("Furball", 2011, "Me", lives=2)
    >>> my_cat.talk()
    Meow!
    >>> my_cat.name
    'Furball'
    >>> my_cat.lose_life()
    >>> my_cat.is_alive
    True
    >>> my_cat.eat("poison")
    Meow!
    Furball ate a poison!
    >>> my_cat.is_alive
    False
    >>> my_cat.lose_life()
    'Cat is dead x_x'
    """
    def __init__(self, name, year_of_birth, owner, lives=9):
        assert type(lives) == int and  lives > 0
        "*** YOUR CODE HERE ***"

    def talk(self):
        """A cat says 'Meow!' when asked to talk."""
        "*** YOUR CODE HERE ***"

    def lose_life(self):
        """A cat can only lose a life if it has at least one
        life. When there are zero lives left, the 'is_alive'
        variable becomes False.
        """
        "*** YOUR CODE HERE ***"


# Table
class T8ble(obj):
    def __init__(self):
        self.rows = []

    def num_rows():
        """Compute the number of rows in a table"""
        "*** YOUR CODE HERE ***"

    def num_cols():
        """Compute the number of cols in a table"""
        "*** YOUR CODE HERE ***"

    def labels():
        """Lists the column labels in a table"""
        "*** YOUR CODE HERE ***"

    def column(self, label):
        """
        The values of a column
        """
        "*** YOUR CODE HERE ***"

    def select(self, labels):
        """
        Create a copy of a table with only some of the columns.
        Each column is the column name or index.
        """
        "*** YOUR CODE HERE ***"


    def with_column(self, label, values):
        """
        A table with an additional or replaced column.
        label is a string for the name of a column, values is an list
        """
        "*** YOUR CODE HERE ***"


    def sort(self, column, descending=True):
        """
        Create a copy of a table sorted by the values in a column.
        Defaults to ascending order unless descending = True is included.
        """
        "*** YOUR CODE HERE ***"


    def where(self, label, filter_fn):
        """
        Create a copy of a table with only the rows that match a filter function.
        """
        "*** YOUR CODE HERE ***"


