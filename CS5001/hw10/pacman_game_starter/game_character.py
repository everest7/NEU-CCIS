
class GameCharacter:
    """Game character class. This contains code that is common to
all characters in the game."""

    def display(self):
        """Display the character. When the character approaches the
edge of the screen, draw the character twice, once going
off and once coming on the other edge"""
        # Call the update method implemented by the extending class
        self.update()

        # Based on the size of the view area and the size of the
        # character, we need to draw the character multiple times when
        # the character moves off the edge of the view area.
        if (self.x > self.maze.WIDTH + self.CHAR_WIDTH/2):
            self.x = self.CHAR_WIDTH/2
        elif (self.x > self.maze.WIDTH - self.CHAR_WIDTH/2):
            self.draw_self(self.x - self.maze.WIDTH, self.y)

        if (self.y > self.maze.HEIGHT + self.CHAR_HEIGHT/2):
            self.y = self.CHAR_HEIGHT/2
        elif (self.y > self.maze.HEIGHT - self.CHAR_HEIGHT/2):
            self.draw_self(self.x, self.y - self.maze.HEIGHT)

        if (self.x < -(self.CHAR_WIDTH/2)):
            self.x = self.maze.WIDTH - self.CHAR_WIDTH/2
        elif (self.x < self.CHAR_WIDTH/2):
            self.draw_self(self.x + self.maze.WIDTH, self.y)

        if (self.y < -(self.CHAR_WIDTH/2)):
            self.y = self.maze.HEIGHT - self.CHAR_HEIGHT/2
        elif (self.y < self.CHAR_HEIGHT/2):
            self.draw_self(self.x, self.y + self.maze.HEIGHT)

        # In all other cases, draw the character once
        self.draw_self(self.x, self.y)
