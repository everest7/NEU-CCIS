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
        """Initialize WordLadder class with five attributes
        Args:
            w1: user input word one
            w2: user input word two
            wordlist: a list of legal english word with a specified length
        """
        self.w1 = w1
        self.w2 = w2
        self.wordlist = wordlist
        self.wordqueue = Queue()
        self.top_stack = Stack()
        self.top_stack.push(w1)
        self.wordqueue.enqueue(self.top_stack)

    def make_ladder(self):
        """Create word ladder between two words
        Returns:
            A stack containing varying words that make up a word ladder
        """
        created_word = {self.w1}
        copy_word_list = self.wordlist.copy()
        while not self.wordqueue.isEmpty():
            top_stack = self.wordqueue.dequeue()
            word = top_stack.peek()
            for i in range(len(word)):
                for ch in ascii_lowercase:
                    if ch != word[i]:
                        new_word = word[: i] + ch + word[i + 1:]
                        if (new_word in copy_word_list and
                                new_word not in created_word):
                            copy_word_list.remove(new_word)
                            created_word.add(new_word)
                            new_stack = top_stack.copy()
                            new_stack.push(new_word)
                            if new_word == self.w2:
                                return new_stack
                            else:
                                self.wordqueue.enqueue(new_stack)
                                if self.wordqueue.isEmpty():
                                    return None
