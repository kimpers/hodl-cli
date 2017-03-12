"""Persistence of transactions"""


class DB:
    """DB persists transactions"""

    def __init__(self):
        self.data = []

    def get_transactions(self):
        """Get all transactions"""
        return self.data[:]

    def add(self, transation):
        """Adds a new transaction"""
        self.data.append(transation)

    def remove(self, transation):
      """Removes a previous transaction"""
      self.data.remove(transation)

    def clear(self):
        """Resets the database"""
        self.data = []
