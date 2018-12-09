def add_list(list):
    """Add a list of numbers recursively
    Args:
        list: a list of number
    Returns:
        the sum of numbers in the list"""
    if len(list) == 0:
        return 0
    else:
        return add_list(list[1:]) + list[0]


list = [1, 2, 3, 4, 5]
print(add_list(list))
