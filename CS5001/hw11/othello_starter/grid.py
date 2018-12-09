class Grid:
    def __init__(self, WIDTH, HEIGHT, SPACING):
        """Initialize the checkerboard as grids"""
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.SPACING = SPACING

    def display(self):
        """Draw the grid"""
        for i in range(1, self.WIDTH // self.SPACING):
            strokeWeight(2)
            line(0, self.SPACING * i, self.WIDTH, self.SPACING * i)
        for j in range(1, self.HEIGHT // self.SPACING):
            strokeWeight(2)
            line(self.SPACING * j, 0, self.SPACING * j, self.HEIGHT)
