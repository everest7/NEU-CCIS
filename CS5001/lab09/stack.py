
class Stack:
    """A stack class"""
    def __init__(self):
        # we can use a python list as the underlying
        # representation, but this is an implementational
        # choice. We do not have to use a list, we just need
        # to make sure we have an ordered collection and are
        # always able to access the first and the last.
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            return None

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            return None
