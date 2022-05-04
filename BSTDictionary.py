class BSTNode:
    """
    Define a binary tree node class.
    """

    def __init__(self, key, value):
        """
        this function initialize a binary tree
        :param key:
        :param value:
        """
        self.key = key
        self.data = value
        self.left = None
        self.right = None


def judge(obj) -> bool:
    """
    this function shows whether it is a number
    :param obj:
    :return:
    """
    return type(obj) is int


def compare(a, b) -> int:
    """
    this function compares a with b
    :param a:
    :param b:
    :return:
    """
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


class BSTDictionary:
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
 
    def next(self) -> object:
        """
        return the next key
        :rtype: kv
        """
        self._index = self._index + 1
        if self._index >= len(self._all_key):
            return None
        return self.get(self._all_key[self._index])

    def hasNext(self) -> bool:
        """
        return whether we have a next key
        :rtype: bool
        """
        return self._index < len(self._all_key)

    def is_empty(self) -> bool:
        """
        return whether the bit is empty
        :rtype: bool
        """
        return self._root is None

    # Find value according to key value
    def get(self, key):
        """
        get value by key
        :param key:
        :return:
        """
        cur_node = self._root
        while cur_node:
            if compare(cur_node.key, key) == 1:
                cur_node = cur_node.left
            elif compare(cur_node.key, key) == 2:
                cur_node = cur_node.right
            else:
                return cur_node.data
        return None

    def put(self, key, value):
        """
        put V<key,value> to dictionary
        :param key:
        :param value:
        :return:
        """
        if self.is_empty():
            self._root = BSTNode(key, value)
            self._all_key.append(key)
        cur_node = self._root
        while True:
            if compare(cur_node.key, key) == 1:
                if cur_node.left is None:
                    cur_node.left = BSTNode(key, value)
                    self._all_key.append(key)
                cur_node = cur_node.left
            elif compare(cur_node.key, key) == 2:
                if cur_node.right is None:
                    cur_node.right = BSTNode(key, value)
                    self._all_key.append(key)
                cur_node = cur_node.right
            else:
                cur_node.data = value
                break

    def remove(self, key):
        """
        remove V by key from dictionary
        :param key:
        :return:
        """
        p, q = None, self._root
        # if the tree is None, return
        if not q:
            return
        # q is the node we need to find, q is the parent node of q
        while q and q.key != key:
            p = q
            if compare(q.key, key) == 1:
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
        :param node:
        :return:
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
    def to_list(self) -> list:
        """
        convert dictionary to list that contains key and data.
        :return:
        """
        res = []
        if self._root is None:
            return []
        else:
            for node in self._mid_order():
                res.append((node.key, node.data))
            return list(res)

    def to_key_list(self):
        """
        convert dictionary to list that only contains key
        :return:
        """
        res = []
        if self._root is None:
            return []
        else:
            for node in self._mid_order():
                res.append(node.key)
            return list(res)

    def from_list(self, e):
        """
        convert list to dictionary
        :param e:
        :return:
        """
        if e:
            for element in e:
                self.put(element[0], element[1])

    def size(self) -> int:
        """
        get the number of storage elements in dictionary
        :return:
        """
        return len(self.to_list())

    def filter(self, f):
        """
        filter the diction by judge function
        :param f:
        :return:
        """
        stack = []
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

    def member(self, key) -> bool:
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
        """
        clear all elements in the dictionary.
        :return:
        """
        self._root = None
        self._index = -1
        self._all_key = []

    def concat(self, dic):
        """
        merge two dictionaries into one.
        :param dic:
        :return:
        """
        assert type(dic) is BSTDictionary
        self_key = []
        concat_key = []
        flag = 0
        while len(self_key) > 0:
            if self_key.pop() < concat_key.pop():
                flag = 1
                break
        if self.size() > dic.size():
            ls = dic.to_list()
            for kv in ls:
                self.put(kv[0], kv[1])
            return self
        elif self.size() < dic.size():
            ls = self.to_list()
            for kv in ls:
                dic.put(kv[0], kv[1])
            return dic
        elif self.size() < dic.size() and flag == 1:
            ls = dic.to_list()
            for kv in ls:
                self.put(kv[0], kv[1])
            return self
        else:
            ls = self.to_list()
            for kv in ls:
                dic.put(kv[0], kv[1])
            return dic
