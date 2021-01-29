
'''
* File Name : test_random_game.py

* Language : Python

* Creation Date : 06-01-2021

* Last Modified : Wed Jan  6 22:46:17 2021

* Created By : David Hanson

'''

import unittest
import random_game


class TestMain(unittest.TestCase):
    def test_input(self):
        result = random_game.run_guess(5, 5)
        self.assertTrue(result)

    def test_wrong_input(self):
        result = random_game.run_guess(5, 3)
        self.assertFalse(result)

    def test_types(self):
        result = random_game.run_guess('animal', 'hello')
        self.assertIsInstance(result, ValueError)

    def test_out_range(self):
        result = random_game.run_guess(12, 4)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
