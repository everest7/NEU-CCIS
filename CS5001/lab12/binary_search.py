def binary_search(value, list, left, right):
    """Recursive binary search
    Args:
        value: value you're searching for
        list: a list where you're searching
        left: the begining index of list
        right: the ending index of list
    Return:
    the index of value: if the value exists in the list
    -1: if the value does not exist in the list"""
    mid = (left + right) // 2
    if mid >= len(list) - 1:
        return -1
    elif list[mid] == value:
        return mid
    elif list[mid] < value:
        return binary_search(value, list, mid + 1, right)
    elif list[mid] > value:
        return binary_search(value, list, left, mid - 1)


list = [1, 2, 3, 4, 5, 6, 7]
print(binary_search(5, list, 0, len(list) - 1))
print(binary_search(8, list, 0, len(list) - 1))
