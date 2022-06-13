from typing import List, Tuple, Callable, Optional


class BSTNode:
    """
    Define a binary tree node class.
    """

    def __init__(self, key: Optional[int], value: Optional[int]) -> None:
        if type(key) is not int and key is not None:
            raise TypeError("key and value only can be int or None")
        elif type(value) is not int and value is not None:
            raise TypeError("key and value only can be int or None")
        self.key: Optional[int] = key
        self.data: Optional[int] = value
        self.left = None
        self.right = None


class DIterator(object):

    def __init__(self, lst: List[Tuple[Optional[int], Optional[int]]]) -> None:
        self.__index = -1
        self.__chunk = lst

    def next(self) -> Tuple[Optional[int], Optional[int]]:
        """
        return the next value
        """
        self.__index = self.__index + 1
        if self.__index >= len(self.__chunk):
            raise StopIteration
        return self.__chunk[self.__index]

    def hasNext(self) -> bool:
        """
        return whether we have a next key
        :rtype: bool
        """
        return self.__index < len(self.__chunk)


class BSTDictionary:
    """
    Binary sort tree based on bst-node class.
    """

    def __init__(self) -> None:
        """
        init dictionary
        we use a list to implement pseudo iterator
        """
        self._root: Optional[BSTNode] = None
        self._all_key: List[int] = []
        self._index = -1

    def __iter__(self):
        """ iterator object """
        return DIterator(self.to_list())

    def is_empty(self) -> bool:
        """ Judge whether the Dictionary is empty"""
        return self._root is None

    def get(self, key: Optional[int]) -> object:
        """
        get value by key
        """
        cur_node = self._root
        while cur_node:
            if cur_node.key > key:
                cur_node = cur_node.left
            elif cur_node.key < key:
                cur_node = cur_node.right
            else:
                return cur_node.data
        return None

    def put(self, key: Optional[int], value: Optional[int]) -> None:
        """
        put V<key,value> to dictionary
        """
        if self.is_empty():
            self._root = BSTNode(key, value)
            self._all_key.append(key)
        cur_node = self._root
        while True:
            if cur_node.key > key:
                if cur_node.left is None:
                    cur_node.left = BSTNode(key, value)
                    self._all_key.append(key)
                cur_node = cur_node.left
            elif cur_node.key < key:
                if cur_node.right is None:
                    cur_node.right = BSTNode(key, value)
                    self._all_key.append(key)
                cur_node = cur_node.right
            else:
                cur_node.data = value
                break

    def remove(self, key: Optional[int]) -> None:
        """
        remove V by key from dictionary
        """
        p, q = None, self._root
        """ if the tree is None, return"""
        if not q:
            return
        """q is the node we need to find, q is the parent node of q"""
        while q and q.key != key:
            p = q
            if q.key > key:
                q = q.left
            else:
                q = q.right
            if not q:
                return
        self._all_key.remove(q.key)
        """ Readjust the binary tree structure
        Find the rightmost node of the left subtree of node q
        link the right subtree of q to the right subtree of this node"""
        if not q.left:
            if p is None:
                self._root = q.right
            elif q is p.left:
                p.left = q.right
            else:
                p.right = q.right
            return
        r = q.left
        while r.right:
            r = r.right
        r.right = q.right
        if p is None:
            self._root = q.left
        elif p.left is q:
            p.left = q.left
        else:
            p.right = q.left

    def _mid_order(self, node: BSTNode = None) -> List[BSTNode]:
        """
        Middle order traversal binary tree to get V<key,value> for each node
        """

        if node is None:
            node = self._root
        if node.left is not None:
            for item in self._mid_order(node.left):
                yield item
        yield node
        if node.right is not None:
            for item in self._mid_order(node.right):
                yield item

    """ Store all the values in the dictionary in the linked list """

    def to_list(self) -> List[Tuple[Optional[int], Optional[int]]]:
        """
        convert dictionary to a list
        :return: the list convert by dictionary
        """
        res: List[Tuple[Optional[int], Optional[int]]] = []
        if self._root is None:
            return res
        else:
            for node in self._mid_order():
                res.append((node.key, node.data))
            return res

    def to_key_list(self) -> List[Optional[int]]:
        """
        return a list containing all keys
        :return: the list convert by all  key in dictionary
        """
        res: List[Optional[int]] = []
        if self._root is None:
            return []
        else:
            for node in self._mid_order():
                res.append(node.key)
            return res

    def from_list(self, e: List[Tuple[Optional[int], Optional[int]]]) -> None:
        """
        Turn a list containing tuples into a dictionary
        :param e: A list containing tuples
        """
        if e:
            for element in e:
                self.put(element[0], element[1])

    def size(self) -> int:
        """
        Returns the number of key value pairs contained in the dictionary
        """
        return len(self.to_list())

    def filter(self, f: Callable[[Optional[int]], bool]) -> None:
        """
        :param f: filter function
        """
        stack: List[BSTNode] = []
        node = self._root
        result = []
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if not f(node.data):
                result.append(node.key)
            node = node.right
        for key in result:
            self.remove(key)

    def member(self, key: Optional[int]) -> bool:
        """
        Query whether the key exists in the dictionary
        :param key:
        """
        return self.get(key) is not None

    def map(self, f: Callable[[Optional[int]], Optional[int]]) -> None:
        """
        Use function f to process all value in the dictionary
        :param f: function
        """
        stack: List[BSTNode] = []
        node = self._root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            node.data = f(node.data)
            node = node.right

    def reduce(self, f: Callable[[int, Optional[int]], int],
               initial_state: int = 0) -> object:
        """
        Use function f to process all value in the dictionary
        :param initial_state:
        :param f: function
        :return: state
        """
        state: int = initial_state
        stack: List[BSTNode] = []
        node: 'BSTNode' = self._root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            state = f(state, node.data)
            node = node.right
        return state

    def empty(self) -> None:
        """
        Remove all contents of dictionary
        """
        self._root = None
        self._index = -1
        self._all_key = []

    def concat(self, dic: 'BSTDictionary') -> 'BSTDictionary':
        """
        Merge two dictionaries
        """
        assert type(dic) is BSTDictionary
        for i in dic.to_list():
            self.put(i[0], i[1])
