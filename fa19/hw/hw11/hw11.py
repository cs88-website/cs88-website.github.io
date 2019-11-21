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

