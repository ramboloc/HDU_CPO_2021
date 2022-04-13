import types
import unittest
from hypothesis import given
import hypothesis.strategies as st
from mutable import *

from Dictionary import *


def judge(obj):
    """this function shows whether it is a number """
    return type(obj) is int


def f(x):
    """"this function transform the type of x to str """
    return str(x)


def add_value(obj, value):
    """this function add all value if type of value is int """
    if type(value) is int:
        return obj + value
    else:
        return obj


class TestMutableDictionary(unittest.TestCase):

    def test_set(self):
        dictionary_test = Dictionary()
        self.assertEqual(dictionary_test.get(1), None)
        dictionary_test.put(1, 541)
        self.assertEqual(dictionary_test.get(1), 541)

    def test_size(self):
        dictionary_test = Dictionary()
        size = dictionary_test.size()
        self.assertEqual(size, 0)
        dictionary_test.put(1, "sd")
        self.assertEqual(dictionary_test.size(), 1)
        dictionary_test.put(2, 2)
        self.assertEqual(dictionary_test.size(), 2)

    def test_get(self):
        dictionary_test = Dictionary()
        self.assertEqual(dictionary_test.get(1), None)
        dictionary_test.put(1, 123)
        dictionary_test.put(123, 123)
        self.assertEqual(dictionary_test.get(1), 123)
        self.assertEqual(dictionary_test.get(123), 123)

    def test_remove(self):
        dictionary_test = Dictionary()
        dictionary_test.put(1, 11)
        dictionary_test.put(2, 22)
        dictionary_test.put(3, 33)
        self.assertEqual(dictionary_test.get(1), 11)
        dictionary_test.remove(1)
        self.assertEqual(dictionary_test.get(1), None)

    def test_to_list(self):
        dictionary_test = Dictionary()
        self.assertEqual(dictionary_test.to_list(), [])
        dictionary_test.put(1, 11)
        dictionary_test.put(2, 22)
        dictionary_test.put(3, 33)
        self.assertEqual(dictionary_test.to_list(), [[1, 11], [2, 22], [3, 33]])

    def test_from_list(self):
        test_data = [[], [[1, 11]], [[1, 11], [2, 21]]]
        for e in test_data:
            dictionary_test = Dictionary()
            dictionary_test.from_list(e)
            self.assertEqual(dictionary_test.to_list(), e)

    def test_filter(self):
        dictionary_test = Dictionary()
        dictionary_test.put(1, 11)
        dictionary_test.put(2, "22")
        dictionary_test.put(3, 33)
        dictionary_test.filter(judge)
        self.assertEqual(dictionary_test.to_list(), [[1, 11], [3, 33]])

    def test_member(self):
        dictionary_test = Dictionary()
        dictionary_test.put(1, 11)
        dictionary_test.put(2, "22")
        dictionary_test.put(3, 33)
        self.assertEqual(dictionary_test.member(4), False)
        self.assertEqual(dictionary_test.member(3), True)

    def test_map(self):
        dictionary_test = Dictionary()
        dictionary_test.put(1, 11)
        dictionary_test.put(2, 22)
        dictionary_test.map(f)
        self.assertEqual(dictionary_test.to_list(), [[1, "11"], [2, "22"]])

    def test_reduce(self):
        dictionary_test = Dictionary()
        dictionary_test.put(1, 11)
        dictionary_test.put(2, "22")
        dictionary_test.put(3, 33)
        self.assertEqual(dictionary_test.reduce(add_value, initial_state=0), 44)


if __name__ == '__main__':
    unittest.main()
