from die import Die
import random as r


class PairOfDice:
    """Creating a pair od dice"""
    # Initializing two dice by giving them a random number
    num1 = r.randint(1, 6)
    num2 = r.randint(1, 6)
    die1 = Die(num1)
    die2 = Die(num2)

    def __init__(self):
        self.sum = 0

    def roll_dice(self):
        """Rolling two dice"""
        self.die1.current_value = self.die1.roll()
        self.die2.current_value = self.die2.roll()

    def current_value(self):
        """Return the sum of two dice's value"""
        self.sum = self.die1.current_value + self.die2.current_value
        return self.sum
