
class GameController:
    """Maintains the state of the game."""
    def __init__(self, WIDTH, HEIGHT):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.player_wins = False
        self.pinky_wins = False

    def update(self):
        """Carries out necessary actions if pinky or player wins"""
        if self.pinky_wins:
            fill(1)
            textSize(50)
            text("PINKY WINS", self.WIDTH/2 - 140, self.HEIGHT/2)
        if self.player_wins:
            fill(1)
            textSize(50)
            text("YOU WIN!!!", self.WIDTH/2 - 140, self.HEIGHT/2)
