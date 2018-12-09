def linear_search(value, list, counter):
    """Recursive linear search
    Args:
        value: value you're searching
        list: a list where you're searching
        counter: track the recursion
    Returns:
        the index of value: if value exists in the list
        -1: if value does not exists in the list"""
    if len(list) <= 0:
        return -1
    elif value == list[0]:
        return counter
    else:
        counter += 1
        return linear_search(value, list[1:], counter)


list = [3, 5, 7, 2, 6]
print(linear_search(5, list, 0))
print(linear_search(8, list, 0))
