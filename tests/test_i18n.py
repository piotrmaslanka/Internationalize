import unittest
from internationalize import add, add_to_kw, get_for


class I18nTestCase(unittest.TestCase):
    def test_internationalize(self):
        add({'hello': {'pl': 'Witaj', 'en': 'Hello'}})
        self.assertEqual(get_for('hello')['en'], 'Hello')

        add({'hello': {'de': 'Hallo'}})
        self.assertEqual(get_for('hello')['de'], 'Hallo')
        self.assertEqual(get_for('hello')['en'], 'Hello')
        self.assertRaises(KeyError, lambda: self.assertEqual(get_for('hello')['it'], 'Hello'))


if __name__ == '__main__':
    unittest.main()
