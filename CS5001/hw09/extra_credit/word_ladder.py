from queue import Queue
from stack import Stack
from string import ascii_lowercase


class WordLadder:
    """A class providing functionality to create word ladders"""
    stack = Stack()
    # TODO:
    # Implement whatever functionality is necessary to generate a
    # stack representing the word ladder based on the parameters
    # passed to the constructor.

    def __init__(self, w1, w2, wordlist):
        self.w1 = w1
        self.w2 = w2
        self.wordlist = wordlist
        self.wordqueue = Queue()
        self.top_stack = Stack()
        self.top_stack.push(w1)
        self.wordqueue.enqueue(self.top_stack)

    def make_ladder(self):
        created_word = {self.w1}
        copy_list = self.wordlist.copy()
        while not self.wordqueue.isEmpty():
            top_stack = self.wordqueue.dequeue()
            word = top_stack.peek()
            if word == self.w2:
                return top_stack
            for i in range(len(word)):
                for ch in ascii_lowercase:
                    if ch != word[i]:
                        new_word = word[: i] + ch + word[i + 1:]
                        if (new_word in copy_list and
                                new_word not in created_word):
                            copy_list.remove(new_word)
                            created_word.add(new_word)
                            new_stack = top_stack.copy()
                            new_stack.push(new_word)
                            self.wordqueue.enqueue(new_stack)
                            if self.wordqueue.isEmpty():
                                return None
                        if i == 0:
                            new_word_ins = ch + word
                        elif i == len(word) - 1:
                            new_word_ins = word + ch
                        else:
                            new_word_ins = word[: i] + ch + word[i:]
                        if (new_word_ins in copy_list and
                                new_word_ins not in created_word):
                            copy_list.remove(new_word_ins)
                            created_word.add(new_word_ins)
                            new_stack = top_stack.copy()
                            new_stack.push(new_word_ins)
                            self.wordqueue.enqueue(new_stack)
                            if self.wordqueue.isEmpty():
                                return None
                        if i == 0:
                            new_word_del = word[1:]
                        elif i == len(word) - 1:
                            new_word_del = word[:i - 1]
                        else:
                            new_word_del = word[: i] + word[i + 1:]
                        if (new_word_del in copy_list and
                                new_word_del not in created_word):
                            copy_list.remove(new_word_del)
                            created_word.add(new_word_del)
                            new_stack = top_stack.copy()
                            new_stack.push(new_word_del)
                            self.wordqueue.enqueue(new_stack)
                            if self.wordqueue.isEmpty():
                                return None
