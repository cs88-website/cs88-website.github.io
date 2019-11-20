class Account(object):
    """A bank account that allows deposits and withdrawals.

    >>> sophia_account = Account('Sophia')
    >>> sophia_account.deposit(1000000)   # depositing my paycheck for the week
    1000000
    >>> sophia_account.transactions
    [('deposit', 1000000)]
    >>> sophia_account.withdraw(100)      # buying dinner
    999900
    >>> sophia_account.transactions
    [('deposit', 1000000), ('withdraw', 100)]
    """

    interest = 0.02
    balance = 1000

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
        self.transactions = []

    def deposit(self, amount):
        """Increase the account balance by amount and return the
        new balance.
        """
        self.transactions.append(('deposit', amount))
        Account.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        """Decrease the account balance by amount and return the
        new balance.
        """
        self.transactions.append(('withdraw', amount))
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = Account.balance - amount
        return Account.balance


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



class Error:
    """
    >>> err1 = Error(12, "error.py")
    >>> err1.write()
    'error.py:12'

    """
    def __init__(self, line, file):
        "*** YOUR CODE HERE ***"

    def write(self):
        return self.file + ':' + str(self.line)

class SyntaxError(Error):
    """
    >>> err1 = SyntaxError(17, "HW10.py")
    >>> err1.write()
    HW10.py:17 SyntaxError : Invalid syntax
    >>> err1.add_code(4, "EOL while scanning string literal")
    >>> err2 = SyntaxError(18, "HW10.py", 4)
    >>> err2.write()
    HW10.py:18 SyntaxError : EOL while scanning string literal

    """
    type = 'SyntaxError'
    msgs = {0 : "Invalid syntax", 1: "Unmatched parentheses", 2: "Incorrect indentation", 3: "missing colon"}

    def __init__(self, line, file, code=0):
        "*** YOUR CODE HERE ***"

    def write(self):
        end = self.type + ' : ' + self.message
        "*** YOUR CODE HERE ***"

    def add_code(self, code, msg):
        "*** YOUR CODE HERE ***"

class ZeroDivisionError(Error):
    """
    >>> err1 = ZeroDivisionError(273, "HW10.py")
    >>> err1.write()
    HW10.py:273 ZeroDivisionError : division by zero
    """
    type = 'ZeroDivisionError'

    def __init__(self, line, file, message='division by zero'):
        "*** YOUR CODE HERE ***"

    def write(self):
        end = self.type + ' : ' + self.message
        "*** YOUR CODE HERE ***"


class Mint:
    """A mint creates coins by stamping on years.

    The update method sets the mint's stamp to Mint.current_year.

    >>> mint = Mint()
    >>> mint.year
    2015
    >>> dime = mint.create(Dime)
    >>> dime.year
    2015
    >>> Mint.current_year = 2100  # Time passes
    >>> nickel = mint.create(Nickel)
    >>> nickel.year     # The mint has not updated its stamp yet
    2015
    >>> nickel.worth()  # 5 cents + (85 - 50 years)
    40
    >>> mint.update()   # The mint's year is updated to 2100
    >>> Mint.current_year = 2175     # More time passes
    >>> mint.create(Dime).worth()    # 10 cents + (75 - 50 years)
    35
    >>> Mint().create(Dime).worth()  # A new mint has the current year
    10
    >>> dime.worth()     # 10 cents + (160 - 50 years)
    120
    >>> Dime.cents = 20  # Upgrade all dimes!
    >>> dime.worth()     # 20 cents + (160 - 50 years)
    130


    """
    current_year = 2015

    def __init__(self):
        self.update()

    def create(self, kind):
        "*** YOUR CODE HERE ***"

    def update(self):
        "*** YOUR CODE HERE ***"

class Coin:
    def __init__(self, year):
        self.year = year

    def worth(self):
        "The worth is a coin's face value + 1 cent for each year over age 50."
        "*** YOUR CODE HERE ***"

class Nickel(Coin):
    cents = 5

class Dime(Coin):
    cents = 10

