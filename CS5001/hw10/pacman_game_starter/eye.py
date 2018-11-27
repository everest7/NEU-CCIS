
class Eye:
    """A ghost eye"""
    def __init__(self):
        # Direction is a tuple
        self.direction = (0, 0)

    def look(self, direction):
        """Sets eye direction"""
        self.direction = direction

    def display(self, x, y):
        """Draws ghost's eye"""
        noStroke()
        fill(1)
        ellipse(x, y, 30, 30)
        fill(0, 0, 1)
        ellipse(x + (self.direction[0])*5, y + (self.direction[1]*5), 10, 10)
