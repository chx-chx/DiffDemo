# test.py
# coding:utf-8

import unittest


def add(a, b):
    return a + b


def division_numb(a, b):
    return a / b


class Test(unittest.TestCase):
    def test_add_1(self):
        self.assertEqual(add(1, 1), 2)

    def test_add_2(self):
        self.assertEqual(add(2, 0), 1)

    # def test_division_1(self):
    #     self.assertEqual(division_numb(2, 1), 2)
    #
    # def test_division_2(self):
    #     self.assertEqual(division_numb(2, 0), 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
