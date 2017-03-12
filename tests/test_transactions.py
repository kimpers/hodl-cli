# pylint: skip-file
from .context import Transactions, Transaction, Currency, Type

import unittest


class DBTestSuite(unittest.TestCase):

    def test_buy(self):
        ledger = Transactions()
        ledger.buy(100, Currency.EUR, Currency.ETH)
        ledger.buy(200, Currency.EUR, Currency.ETH)
        transactions = ledger.get_transactions()
        self.assertEqual(len(transactions), 2)
        self.assertTrue(transactions[0] == Transaction(Type.BUY, Currency.EUR,
                                                       Currency.ETH, 100))
        self.assertTrue(transactions[1] == Transaction(Type.BUY, Currency.EUR,
                                                       Currency.ETH, 200))

    def test_sell(self):
        ledger = Transactions()
        ledger.buy(200, Currency.EUR, Currency.ETH)
        ledger.sell(100, Currency.EUR, Currency.ETH)
        transactions = ledger.get_transactions()
        self.assertEqual(len(transactions), 2)
        self.assertTrue(transactions[0] == Transaction(Type.BUY, Currency.EUR,
                                                       Currency.ETH, 200))
        self.assertTrue(transactions[1] == Transaction(Type.SELL, Currency.EUR,
                                                       Currency.ETH, 100))

if __name__ == '__main__':
    unittest.main()
