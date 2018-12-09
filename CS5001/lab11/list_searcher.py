import random


class ListSearcher:
    """Implements several search algorithms"""
    DEFAULT_SIZE = 10

    def __init__(self, size=DEFAULT_SIZE):
        self.size = size
        self.comparisons = 0

    def generate_data(self, ordered=True):
        """Generate a new ordered or unordered list to experiment on"""
        self._list = list(range(self.size))
        if not ordered:
            random.shuffle(self._list)

    def linear_search(self, key):
        """
        Run linear search for key.
        Return the index of the key.
        """
        for i in range(len(self._list)):
            self.comparisons += 1
            if self._list[i] == key:
                return i
        return -1

    def binary_search(self, key):
        """
        Run binary search for key.
        Return the index of the key.
        """
        left = 0
        right = len(self._list) - 1
        while(left <= right):
            self.comparisons += 1
            mid = int((left+right)/2)
            if key == self._list[mid]:
                return mid
            elif key > self._list[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def find_median(self):
        """
        Find the median value in an unsorted list.
        Return the index of the median value in the list.
        """
        for i in range(len(self._list)):
            less_than = 0  # counts numbers less than self._list[i]
            grt_than = 0  # counts numbers greater than self._list[i]
            for j in range(len(self._list)):
                self.comparisons += 1
                if (self._list[j] < self._list[i]):
                    less_than += 1

                elif (self._list[j] > self._list[i]):
                    grt_than += 1

            # If the list has odd length, there is a unique median
            if (len(self._list) % 2 == 1 and less_than == grt_than):
                return i
            # If the list has even length, there are 2 medians. We
            # return the first one that we come across.
            elif (len(self._list) % 2 == 0 and less_than == grt_than - 1):
                return i
            self.comparisons += 1
        # If the list is empty, no median index will be returned
        return -1

    def reset_comparisons(self):
        self.comparisons = 0
