# pylint: skip-file
from .context import DB

import unittest


class DBTestSuite(unittest.TestCase):

    def test_add(self):
        db = DB()
        db.add('A')
        self.assertEqual(db.get_transactions(), ['A'])

    def test_remove(self):
        db = DB()
        db.add('A')
        db.add('B')
        db.remove('A')
        self.assertEqual(db.get_transactions(), ['B'])

    def test_clear(self):
        db = DB()
        db.add('A')
        db.clear()
        self.assertEqual(db.get_transactions(), [])


if __name__ == '__main__':
    unittest.main()
