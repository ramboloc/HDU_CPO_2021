def f(x) -> str:
    """
    this function transform the type of x to str
    """
    return str(x)


def add_value(obj, value) -> object:
    """
    this function add all value if type of value is int
    """
    if type(value) is int:
        return obj + value
    else:
        return obj


def list_to_kv_list(list1) -> list:
    """
    Convert a list containing two tuples into kV we require_ list
    kv_ List shall have the following characteristics:
    1. All elements are binary.
    2. All element key values are not duplicate.
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


def list_merge(lis1, lis2) -> list:
    """
    merge tow list to one according to list length
    """
    for i in lis2:
        lis1.append(i)
    return lis1
