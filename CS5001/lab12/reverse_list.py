def reverse_list(list):
    """Reverse a list recursively
    Args:
        list: a list to be reversed
    Returns:
        reversed list"""
    if len(list) == 0:
        return ''
    else:
        return str(list[-1]) + reverse_list(list[:-1])


list = ['h', 'e', 'l', 'l', 'o']
list2 = [1, 2, 3, 4, 5]
print(reverse_list(list))
print(reverse_list(list2))
