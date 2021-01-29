
'''
* File Name : testing_practice.py

* Language : Python

* Creation Date : 06-01-2021

* Last Modified : Wed Jan  6 17:26:00 2021

* Created By : David Hanson

'''

import unittest
import main2


class TestMain(unittest.TestCase):
    def setUp(self):
        print('about to test a function')

    def test_do_stuff(self):
        '''HIIIIIII'''
        test_param = 10.4
        result = main2.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'sodifse'
        result = main2.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = main2.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')

    def test_do_stuff4(self):
        test_param = ''
        result = main2.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')

    def test_do_stuff5(self):
        test_param = 0
        result = main2.do_stuff(test_param)
        self.assertEqual(result, 5)

    def tearDown(self):
        print('cleaning up')


if __name__ == '__main__':
    unittest.main()
