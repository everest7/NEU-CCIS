def bubble_sort(list, length):
    """Recursive bubble sort
    Args:
        list: a list to be sorted
        length: the length of list you're sorting
    Returns:
        a sorted list"""
    if length == 1:
        return list
    else:
        list = findmax(list, 0, length)
        return bubble_sort(list, length - 1)


def findmax(list, left, right):
    """Find the largest element is a list and put it in the last position
    Args:
        list: a list needed to be operated
        left: begin index of the list
        right: ending index of the list
    Returns:
        a list with largest element in the last position"""
    if left == right:
        return list
    else:
        if left > 0 and list[left] < list[left - 1]:
            list[left], list[left - 1] = list[left - 1], list[left]
        return findmax(list, left + 1, right)


list = [4, 15, 18, 5, 1, 7, 9, 6, 8]
print(bubble_sort(list, len(list)))
list2 = [10, 25, 31, 87, 45, 36, 27]
print(bubble_sort(list2, len(list2)))
