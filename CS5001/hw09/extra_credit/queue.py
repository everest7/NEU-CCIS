

class Queue:
    def __init__(self):
        self.items = []

    def __repr__(self):
        s = "head----------\n"
        for item in self.items:
            s += str(item) + "\n"
        s += "tail----------"
        return s

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0
