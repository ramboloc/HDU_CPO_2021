import unittest
from hypothesis import given
import hypothesis.strategies as st
import BSTDictionary
from  BSTDictionary import *


def f(x):
    """"this function transform the type of x to str """
    return str(x)


def add_value(obj, value):
    """this function add all value if type of value is int """
    if type(value) is int:
        return obj + value
    else:
        return obj


def list_to_kv_list(list1):
    """
    Convert a list containing two tuples into kV we require_ list
    kv_ List shall have the following characteristics:
    1. All elements are binary.
    2. All element key values are not duplicate.
    :param list1:
    :return:
    """
    list_key = []
    list_value = []
    new_list = []
    for i in list1:
        if list_key.__contains__(i[0]) is not True:
            list_key.append(i[0])
            list_value.append(i[1])
        else:
            list_value[list_key.index(i[0])] = i[1]
    index = 0
    for key in list_key:
        new_list.append((key, list_value[index]))
        index = index + 1
    new_list.sort()
    return new_list


def list_merge(lis1, lis2):
    """merge tow list to one according to list length"""
    for i in lis2:
        lis1.append(i)
    return lis1


class TestMutableDictionary(unittest.TestCase):

    def test_set(self):
        dictionary_test = BSTDictionary()
        self.assertEqual(dictionary_test.get(1), None)
        dictionary_test.put(1, 541)
        self.assertEqual(dictionary_test.get(1), 541)

    def test_size(self):
        dictionary_test = BSTDictionary()
        size = dictionary_test.size()
        self.assertEqual(size, 0)
        dictionary_test.put(1, "sd")
        self.assertEqual(dictionary_test.size(), 1)
        dictionary_test.put(2, 2)
        self.assertEqual(dictionary_test.size(), 2)

    def test_get(self):
        dictionary_test = BSTDictionary()
        self.assertEqual(dictionary_test.get(1), None)
        dictionary_test.put(1, 123)
        dictionary_test.put(123, 123)
        self.assertEqual(dictionary_test.get(1), 123)
        self.assertEqual(dictionary_test.get(123), 123)

    def test_remove(self):
        dictionary_test = BSTDictionary()
        dictionary_test.put(1, 11)
        dictionary_test.put(2, 22)
        dictionary_test.put(3, 33)
        self.assertEqual(dictionary_test.get(1), 11)
        dictionary_test.remove(1)
        self.assertEqual(dictionary_test.get(1), None)

    def test_to_list(self):
        dictionary_test = BSTDictionary()
        data = [(1, 11), (2, 22), (3, 33)]
        self.assertEqual(dictionary_test.to_list(), [])
        for e in data:
            dictionary_test.put(e[0], e[1])
        self.assertEqual(dictionary_test.to_list(), data)

    def test_from_list(self):
        test_data = [[], [(1, 11)], [(1, 11), (2, 21)]]
        for e in test_data:
            dictionary_test = BSTDictionary()
            dictionary_test.from_list(e)
            self.assertEqual(dictionary_test.to_list(), e)

    def test_filter(self):
        dictionary_test = BSTDictionary()
        dictionary_test.put(1, 11)
        dictionary_test.put(2, "22")
        dictionary_test.put(3, 33)
        dictionary_test.filter(judge)
        self.assertEqual(dictionary_test.to_list(), [(1, 11), (3, 33)])

    def test_member(self):
        dictionary_test = BSTDictionary()
        dictionary_test.put(1, 11)
        dictionary_test.put(2, "22")
        dictionary_test.put(3, 33)
        self.assertEqual(dictionary_test.member(4), False)
        self.assertEqual(dictionary_test.member(3), True)

    def test_map(self):
        dictionary_test = BSTDictionary()
        dictionary_test.put(1, 11)
        dictionary_test.put(2, 22)
        dictionary_test.map(f)
        self.assertEqual(dictionary_test.to_list(), [(1, "11"), (2, "22")])

    def test_reduce(self):
        dictionary_test = BSTDictionary()
        dictionary_test.put(1, 11)
        dictionary_test.put(2, "22")
        dictionary_test.put(3, 33)
        result = dictionary_test.reduce(add_value, initial_state=0)
        self.assertEqual(result, 44)

    @given(st.lists(st.tuples(st.integers(), st.integers())))
    def test_empty(self, list1):
        new_li = list_to_kv_list(list1)
        dictionary_test = BSTDictionary()
        dictionary_test.from_list(list1)
        self.assertEqual(dictionary_test.to_list(), new_li)
        dictionary_test.empty()
        self.assertEqual(dictionary_test.to_list(), [])

    @given(st.lists(st.tuples(st.integers(), st.integers())),
           st.lists(st.tuples(st.integers(), st.integers())))
    def test_concat(self, list1, list2):
        dictionary_test = BSTDictionary()
        dictionary_test2 = BSTDictionary()
        if len(list1) > len(list2):
            new_list = list_merge(list1, list2)
        else:
            new_list = list_merge(list2, list1)
        new_list = list_to_kv_list(new_list)
        dictionary_test.from_list(list1)
        dictionary_test2.from_list(list2)
        dictionary_test.concat(dictionary_test2)
        self.assertEqual(dictionary_test.to_list(), new_list)
        dictionary_test.empty()
        dictionary_test.from_list(list1)
        dictionary_test2.concat(dictionary_test)
        self.assertEqual(dictionary_test2.to_list(), new_list)


if __name__ == '__main__':
    unittest.main()
