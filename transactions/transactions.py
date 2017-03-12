"""Currency transactions"""
from enum import Enum
from db import DB


class Transactions:
    """Currency Transactions"""
    def __init__(self):
        self.transaction_db = DB()

    def buy(self, amount, from_currency, to_currency):
        """Purchase transaction"""
        transaction = Transaction(Type.BUY, from_currency,
                                  to_currency, amount)
        self.transaction_db.add(transaction)
        return transaction

    def sell(self, amount, from_currency, to_currency):
        """Sell transaction"""
        transaction = Transaction(Type.SELL, from_currency,
                                  to_currency, amount)
        self.transaction_db.add(transaction)
        return transaction

    def get_transactions(self):
        """Gets all saved transactions"""
        return self.transaction_db.get_transactions()


class Type(Enum):
    """ Type of transaction"""
    SELL = -1
    BUY = 1


class Currency(Enum):
    """Currency used for transaction"""
    EUR = 0
    USD = 1
    ETH = 2
    BTC = 3


class Transaction:
    """Represents one currency transaction"""

    def __init__(self, transaction_type, from_currency, to_currency, amount):
        self.transaction_type = transaction_type
        self.from_currency = from_currency
        self.to_currency = to_currency
        self.amount = amount

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return '{}: {} -> {} @ {}'.format(self.transaction_type,
                                          self.from_currency,
                                          self.to_currency,
                                          self.amount)
