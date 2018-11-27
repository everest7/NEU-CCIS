import copy


class Stack:
    def __init__(self):
        self.items = []

    def __str__(self):
        s = ""
        for item in self.items:
            s += str(item) + "\t"
        return s

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0

    def copy(self):
        return copy.deepcopy(self)
