###############
#### Arr88 ####
###############

class Arr88():
    """
    Arr88 is an object similar to Data 8 numpy arrays.
    Here the internel representation is a list
    """
    def __init__(self, values):
        # This checks that all values are the same type, else it errors
        if len(values) > 1:
            assert all([type(values[0]) == type(values[i]) for i in range(len(values))])
        self.values = values

    # DO NOT CHANGE THE __repr__
    # This displays the Arr88 nicely in the terminal
    def __repr__(self):
        return "Arr88(" + str(self.values) + ')'

    def __len__(self):
        """
        Get the length of the Arr88
        >>> arr88 = Arr88([1, 2, 3])
        >>> len(arr88)
        3
        >>> arr88 = Arr88([1, 2, 3, 4])
        >>> len(arr88)
        4
        """
        "*** YOUR CODE HERE ***"
        return ______

    def item(self, i):
        """
        Get the item of the Arr88 at index i
        >>> arr88 = Arr88([1, 2, 3])
        >>> arr88.item(1)
        2
        >>> arr88.item(0)
        1
        """
        "*** YOUR CODE HERE ***"
        return ______

    def __add__(self, arr88):
        """
        Add two Arr88s of the same length componentwise
        >>> arr88a = Arr88([1, 2, 3])
        >>> arr88b = Arr88([4, 5, 6])
        >>> arr88a + arr88b
        Arr88([5, 7, 9])
        >>> arr88a # We aren't mutating arr88a
        Arr88([1, 2, 3])
        >>> arr88a = Arr88(['He', 'Wor', '!'])
        >>> arr88b = Arr88(['llo', 'ld', ''])
        >>> arr88a + arr88b
        Arr88(['Hello', 'World', '!'])
        """
        # Checks that the lengths are the same
        assert len(self) == len(arr88)
        "*** YOUR CODE HERE ***"
        return ______

    def __mul__(self, arr88):
        """
        Multiply two Arr88s of the same length componentwise
        >>> arr88a = Arr88([1, 2, 3])
        >>> arr88b = Arr88([4, 5, 6])
        >>> arr88a * arr88b
        Arr88([4, 10, 18])
        >>> arr88a # We aren't mutating arr88a
        Arr88([1, 2, 3])
        >>> arr88a = Arr88(['Na', 'Batman', '!'])
        >>> arr88b = Arr88([10, 1, 5])
        >>> arr88a * arr88b
        Arr88(['NaNaNaNaNaNaNaNaNaNa', 'Batman', '!!!!!'])
        """
        # Checks that the lengths are the same
        assert len(self) == len(arr88)
        "*** YOUR CODE HERE ***"
        return ______

    def negate(self):
        """
        Negate an Arr88 with mutation
        >>> arr88a = Arr88([1, 2, 3])
        >>> arr88b = Arr88([4.0, -5.5, 0.0])
        >>> arr88a.negate()
        >>> arr88a
        Arr88([-1, -2, -3])
        >>> arr88b.negate()
        >>> arr88b
        Arr88([-4.0, 5.5, -0.0])
        """
        "*** YOUR CODE HERE ***"
        return ______


    def apply(self, func):
        """
        Apply a function to an Arr88
        >>> arr88a = Arr88([1, 2, 3])
        >>> arr88a.apply(lambda x : x * x)
        Arr88([1, 4, 9])
        >>> arr88a # We aren't mutating arr88a
        Arr88([1, 2, 3])
        >>> arr88b = Arr88([lambda x: x, lambda x: x + 1, lambda x: x + 2])
        >>> arr88b.apply(lambda f: f(1))
        Arr88([1, 2, 3])
        """
        "*** YOUR CODE HERE ***"
        return ______




##########################
#### Checking Account ####
##########################

class Account(object):
    """A bank account that allows deposits and withdrawals.

    >>> eric_account = Account('Eric')
    >>> eric_account.deposit(1000000)   # depositing my paycheck for the week
    1000000
    >>> eric_account.transactions
    [('deposit', 1000000)]
    >>> eric_account.withdraw(100)      # buying dinner
    999900
    >>> eric_account.transactions
    [('deposit', 1000000), ('withdraw', 100)]
    """

    interest = 0.02

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
        self.transactions = []

    def deposit(self, amount):
        """Increase the account balance by amount and return the
        new balance.
        """
        self.transactions.append(('deposit', amount))
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        """Decrease the account balance by amount and return the
        new balance.
        """
        self.transactions.append(('withdraw', amount))
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance


class CheckingAccount(Account):
    """A bank account that charges for withdrawals.

    >>> check = Check("Steven", 42)  # 42 dollars, payable to Steven
    >>> steven_account = CheckingAccount("Steven")
    >>> eric_account = CheckingAccount("Eric")
    >>> eric_account.deposit_check(check)  # trying to steal steven's money
    The police have been notified.
    >>> eric_account.balance
    0
    >>> check.deposited
    False
    >>> steven_account.balance
    0
    >>> steven_account.deposit_check(check)
    42
    >>> check.deposited
    True
    >>> steven_account.deposit_check(check)  # can't cash check twice
    The police have been notified.
    """
    withdraw_fee = 1
    interest = 0.01

    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee)



class Check(object):
    "*** YOUR CODE HERE ***"


#########################
#### Vending Machine ####
#########################

class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    """
    def __init__(self, product, price):
        self.product = product
        self.price = price
        self.stock = 0
        self.balance = 0

    "*** YOUR CODE HERE ***"

