class BSTNode:
    """
    Define a binary tree node class.
    It mainly discusses the algorithm, ignoring some problems such as judging the data type.
    """

    def __init__(self, key, value):
        self.key = str(key)
        self.data = value
        self.left = None
        self.right = None


def judge(obj):
    """this function shows whether it is a number """
    return type(obj) is int


def compare(a, b):
    if type(a) == type(b):
        if a > b:
            return 1
        elif a < b:
            return 2
        else:
            return 3
    else:
        if type(a) is int:
            return 1
        else:
            return 2


class Dictionary:
    """
    Binary sort tree based on bst-node class.
    """

    def __init__(self):
        """
        init dictionary
        we use a list to implement pseudo iterator
        """
        self._root = None
        self._all_key = []
        self._index = -1

    def next(self):
        """
        @return the next key
        :rtype: kv
        """
        self._index = self._index + 1
        return self.get(self._all_key[self._index])

    def hasNext(self):
        """
        @return whether we have a next key
        :rtype: bool
        """
        return self._index < len(self._all_key)

    # Judge whether the bit is empty
    def is_empty(self):
        return self._root is None

        # Find value according to key value

    def get(self, key):
        """
        get value by key
        """
        key = str(key)
        cur_node = self._root
        while cur_node:
            if key < cur_node.key:
                cur_node = cur_node.left
            elif key > cur_node.key:
                cur_node = cur_node.right
            else:
                return cur_node.data
        return None

    def put(self, key, value):
        """
        put V<key,value> to dictionary
        """
        key = str(key)
        if self.is_empty():
            self._root = BSTNode(key, value)
            self._all_key.append(key)
        cur_node = self._root
        while True:
            if key < cur_node.key:
                if cur_node.left is None:
                    cur_node.left = BSTNode(key, value)
                    self._all_key.append(key)
                cur_node = cur_node.left

            elif key > cur_node.key:
                if cur_node.right is None:
                    cur_node.right = BSTNode(key, value)
                    self._all_key.append(key)
                cur_node = cur_node.right
            else:

                cur_node.data = value
                return

    def remove(self, key):
        """
        remove V by key from dictionary
        """
        key = str(key)
        p, q = None, self._root
        # if the tree is None, return
        if not q:
            return
        # q is the node we need to find, q is the parent node of q
        while q and q.key != key:
            p = q
            if key < q.key:
                q = q.left
            else:
                q = q.right
            if not q:
                return
        self._all_key.remove(q.key)
        # Readjust the binary tree structure
        # Find the rightmost node of the left subtree of node q
        # link the right subtree of q to the right subtree of this node
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

    def _mid_order(self, node=None):
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

    # Store all the values in the dictionary in the linked list
    def to_list(self):
        res = []
        if self._root is None:
            return []
        else:
            for node in self._mid_order():
                res.append([node.key, node.data])
            return list(res)

    def from_list(self, e):
        assert type(e) is list
        if e:
            for element in e:
                self.put(element[0], element[1])

    def size(self):
        return len(self.to_list())

    def filter(self, judge):
        """filter the diction by judge function"""
        stack = []
        node = self._root
        result = []
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if not judge(node.data):
                result.append(node.key)
            node = node.right
        for key in result:
            self.remove(key)

    def member(self, key):
        """
        Query whether the key exists in the dictionary
        :param key:
        :return:
        """
        return self.get(key) is not None

    def map(self, f):
        """
        Use function f to process all value in the dictionary
        :param f: function
        :return:
        """
        stack = []
        node = self._root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            node.data = f(node.data)
            node = node.right

    def reduce(self, f, initial_state):
        """
        Use function f to process all value in the dictionary
        :param initial_state:
        :param f: function
        :return: state
        """
        state = initial_state
        stack = []
        node = self._root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            state = f(state, node.data)
            node = node.right
        return state

    def empty(self):
        self._root = None
        self._index = -1
        self._all_key = []

    def concat(self, dic):
        assert type(dic) is Dictionary
        if self.size() > dic.size():
            ls = dic.to_list()
            for kv in ls:
                self.put(kv[0], kv[1])
            return self
        else:
            ls = dic.to_list()
            for kv in ls:
                self.put(kv[0], kv[1])
            return dic


# It should be noted that the key will be stored as a string in the dictionary
# the input key will also be  converted into a string during query


if __name__ == '__main__':
    lis = [["1485", 1], [3, 2], [7, 3], [2, 4], [4, 5], [6, 6], [8, 7], [10, 8], [9, 9], [11, 10]]

    dictionary = Dictionary()
    dictionary3 = Dictionary()
    print(dictionary.size())
    for i in range(len(lis)):
        dictionary.put(lis[i][0], lis[i][1])

    # test for init
    print(dictionary.to_list())
    print(dictionary.get("1485"))
    print(dictionary.get(1485))
    print("get a nonexistent value 56 to test:" + str(dictionary.get(56)))
    # test for put
    dictionary.put(99, "put-value1")
    dictionary.put(66, "put-value2")
    dictionary.put(45, "put-value3")
    print("get(99):" + dictionary.get(99))
    print("get(66):" + dictionary.get(66))
    print("get(45):" + dictionary.get(45))
    # test for remove
    dictionary.remove(99)
    print("after remove key 99, the value get(99):" + str(dictionary.get(99)))
    # test whether the put can be overwritten
    print("the old value get(66):" + str(dictionary.get(66)))
    dictionary.put(66, "new-values")
    print("the new value get(66):" + str(dictionary.get(66)))
    # Traversal dictionary
    print(dictionary.to_list())
    print(dictionary3.to_list())
    dictionary4 = dictionary.concat(dictionary3)
