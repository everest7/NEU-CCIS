
class Dot:
    """A dot"""

    def __init__(self, x, y):
        """Dot constructor"""
        self.x = x
        self.y = y

    def display(self):
        """Draws the dot"""
        fill(1, 0.5, 0.0)
        ellipse(self.x, self.y, 10, 10)
