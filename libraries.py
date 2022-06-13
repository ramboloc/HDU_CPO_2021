from typing import List, Optional, Tuple


def list_to_kv_list(list1: List[Tuple[Optional[int],
                                      Optional[int]]]) -> \
        List[Tuple[Optional[int], Optional[int]]]:
    """
    Convert a list containing two tuples into kV we require_ list
    kv_ List shall have the following characteristics:
    1. All elements are binary
    2. All element key values are not duplicate
    """

    list_key: List[Optional[int]] = []
    list_value: List[Optional[int]] = []
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


def list_merge(lis1: List[Tuple[Optional[int], Optional[int]]],
               lis2: List[Tuple[Optional[int], Optional[int]]]) -> \
        List[Tuple[Optional[int], Optional[int]]]:
    """
    merge tow list to one according to list length
    """
    for i in lis2:
        lis1.append(i)
    return lis1
