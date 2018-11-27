from pacman import Pacman
from maze import Maze
from game_controller import GameController


def test_constructor():
    """Test Pacman constructor"""
    game_controller = GameController(600, 400)
    maze = Maze(600, 400, 150, 450,
                100, 300, game_controller)
    pacman = Pacman(maze, game_controller)
    assert pacman.gc is game_controller
    assert pacman.maze is maze
