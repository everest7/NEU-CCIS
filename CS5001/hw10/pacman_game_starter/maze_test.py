from maze import Maze
from game_controller import GameController
from dots import Dots


def test_constructor():
    """Test Maze constructor"""
    g = GameController(600, 400)
    m = Maze(600, 400, 150, 450,
             100, 300, g)
    assert m.LEFT_VERT == 150
    assert m.RIGHT_VERT == 450
    assert m.TOP_HORIZ == 100
    assert m.BOTTOM_HORIZ == 300
    assert m.WIDTH == 600
    assert m.HEIGHT == 400
    assert m.gc is g
    assert m.dots.dots_left() == ((m.dots.WIDTH//m.dots.SPACING + 1) * 2 +
                                  (m.dots.HEIGHT//m.dots.SPACING + 1) * 2)


def test_eat_dots():
    """ Test eat_dots method """
    g = GameController(600, 600)
    m = Maze(600, 600, 150, 450,
             150, 450, g)
    for x_coordinate in range(150, 451, 150):
        for y_coordinate in range(600):
            m.eat_dots(x_coordinate, y_coordinate)
    for y_coordinate in range(150, 451, 150):
        for x_coordinate in range(600):
            m.eat_dots(x_coordinate, y_coordinate)
    assert m.dots.dots_left() == 0
