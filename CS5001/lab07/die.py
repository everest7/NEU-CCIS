import random as r


class Die:

    def __init__(self, current_value):
        self.current_value = current_value

    def roll(self):
        """Roll the dice by giving it a random number"""
        self.current_value = r.randint(1, 6)
        return self.current_value
