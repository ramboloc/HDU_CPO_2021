import unittest
from hypothesis import given
import hypothesis.strategies as st
from BSTDictionary import BSTDictionary
from typing import Optional, List, Tuple
from libraries import list_to_kv_list, list_merge


class TestBSTDictionary(unittest.TestCase):

    def test_set(self) -> None:
        """
        test for function set() in dictionary
        """
        dictionary_test = BSTDictionary()
        self.assertEqual(dictionary_test.get(1), None)
        dictionary_test.put(1, 541)
        self.assertEqual(dictionary_test.get(1), 541)

    def test_size(self) -> None:
        """
        test for function size() in dictionary
        """
        dictionary_test = BSTDictionary()
        size = dictionary_test.size()
        self.assertEqual(size, 0)
        dictionary_test.put(2, 2)
        self.assertEqual(dictionary_test.size(), 1)

    def test_get(self) -> None:
        """
        test for function get() in dictionary
        """
        dictionary_test = BSTDictionary()
        self.assertEqual(dictionary_test.get(1), None)
        dictionary_test.put(1, 123)
        dictionary_test.put(123, 123)
        self.assertEqual(dictionary_test.get(1), 123)
        self.assertEqual(dictionary_test.get(123), 123)

    def test_remove(self) -> None:
        """
        test for function remove() in dictionary
        """
        dictionary_test = BSTDictionary()
        dictionary_test.put(1, 11)
        dictionary_test.put(2, 22)
        dictionary_test.put(3, 33)
        self.assertEqual(dictionary_test.get(1), 11)
        dictionary_test.remove(1)
        self.assertEqual(dictionary_test.get(1), None)

    def test_to_list(self) -> None:
        """
        test for function to_list() in dictionary
        """
        dictionary_test = BSTDictionary()
        data = [(1, 11), (2, 22), (3, 33)]
        self.assertEqual(dictionary_test.to_list(), [])
        for e in data:
            dictionary_test.put(e[0], e[1])
        self.assertEqual(dictionary_test.to_list(), data)

    def test_from_list(self) -> None:
        test_data: List[Tuple[Optional[int], Optional[int]]] = [(1, 11), (2, 21)]
        dictionary_test = BSTDictionary()
        dictionary_test.from_list(test_data)
        self.assertEqual(dictionary_test.to_list(), test_data)

    def test_filter(self) -> None:
        """
        test for function filter() in dictionary
        """
        dictionary_test = BSTDictionary()
        dictionary_test.put(1, 11)
        dictionary_test.put(2, None)
        dictionary_test.put(3, 33)
        dictionary_test.filter(lambda x: x is not None)
        self.assertEqual(dictionary_test.to_list(), [(1, 11), (3, 33)])

    def test_member(self) -> None:
        """
        test for function member() in dictionary
        """
        dictionary_test = BSTDictionary()
        dictionary_test.put(1, 11)
        dictionary_test.put(2, 22)
        dictionary_test.put(3, 33)
        self.assertEqual(dictionary_test.member(4), False)
        self.assertEqual(dictionary_test.member(3), True)

    def test_map(self) -> None:
        """
        test for function map() in dictionary
        """
        dictionary_test = BSTDictionary()
        dictionary_test.put(1, 11)
        dictionary_test.put(2, 22)
        dictionary_test.map(lambda x: x + 1 if x is not None else None)
        self.assertEqual(dictionary_test.to_list(), [(1, 12), (2, 23)])

    def test_reduce(self) -> None:
        """
        test for function reduce() in dictionary
        """
        dictionary_test = BSTDictionary()
        dictionary_test.put(1, 11)
        dictionary_test.put(2, 22)
        dictionary_test.put(3, 33)
        result = dictionary_test.reduce(
            lambda x, y: x + y if y is not None else x, 0)
        self.assertEqual(result, 66)

    @given(st.lists(st.tuples(st.integers(), st.integers())))
    def test_empty(self,
                   list1: List[Tuple[Optional[int], Optional[int]]]) -> None:
        """
        test for function empty() in dictionary
        :param list1: A list containing elements that are tuples
        """
        dictionary_test = BSTDictionary()
        dictionary_test.from_list(list1)
        self.assertEqual(dictionary_test.to_list(), list_to_kv_list(list1))
        dictionary_test.empty()
        self.assertEqual(dictionary_test.to_list(), [])

    @given(st.lists(st.tuples(st.integers(), st.integers())),
           st.lists(st.tuples(st.integers(), st.integers())))
    def test_concat(self, list1: List[Tuple[Optional[int], Optional[int]]],
                    list2: List[Tuple[Optional[int], Optional[int]]]) -> None:
        """
        test for function concat() in dictionary
        :param list1: A list containing elements that are tuples
        :param list2: A list containing elements that are tuples
        """
        dictionary_test = BSTDictionary()
        dictionary_test2 = BSTDictionary()
        new_list = list_merge(list1, list2)
        new_list = list_to_kv_list(new_list)
        dictionary_test.from_list(list1)
        dictionary_test.from_list(list2)
        dictionary_test.concat(dictionary_test2)
        self.assertEqual(dictionary_test.to_list(), new_list)

    @given(st.lists(st.tuples(st.integers(), st.integers())))
    def test_monoid(self,
                    lst: List[Tuple[Optional[int], Optional[int]]]) -> None:
        """
        the function use to test for monoid properties
        """
        dictionary_test = BSTDictionary()
        dictionary_test2 = BSTDictionary()
        dictionary_test2.from_list([])
        dictionary_test2.from_list(lst)
        dictionary_test.concat(dictionary_test2)
        str1 = dictionary_test.to_list()
        dictionary_test.empty()
        dictionary_test.from_list([])
        dictionary_test2.concat(dictionary_test)
        str2 = dictionary_test2.to_list()
        self.assertEqual(str1, str2)


if __name__ == '__main__':
    unittest.main()
