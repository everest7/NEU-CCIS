from pacman import Pacman
from pinky import Pinky
from maze import Maze
from game_controller import GameController

WIDTH = 600
HEIGHT = 600
LEFT_VERT = 150
RIGHT_VERT = 450
TOP_HORIZ = 150
BOTTOM_HORIZ = 450

game_controller = GameController(WIDTH, HEIGHT)
maze = Maze(WIDTH, HEIGHT, LEFT_VERT, RIGHT_VERT,
            TOP_HORIZ, BOTTOM_HORIZ, game_controller)
pacman = Pacman(maze, game_controller)
pinky = Pinky(maze, pacman, game_controller)


def setup():
    size(WIDTH, HEIGHT)
    colorMode(RGB, 1)


def draw():
    background(0)
    maze.display()
    pacman.display()
    pinky.display()
    game_controller.update()


def keyPressed():
    if (key == CODED):
        pacman.control(keyCode)
