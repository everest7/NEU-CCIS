class Grid:
    def __init__(self, WIDTH, HEIGHT, SPACING):
        """Grid constructor"""
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.SPACING = SPACING

    def display(self):
        """Display the grid"""
        for i in range(1, self.WIDTH // self.SPACING):
            strokeWeight(2)
            line(0, self.SPACING * i, self.WIDTH, self.SPACING * i)
        for j in range(1, self.WIDTH // self.SPACING):
            strokeWeight(2)
            line(self.SPACING * j, 0, self.SPACING * j, self.HEIGHT)
