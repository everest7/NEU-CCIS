from dots import Dots
from pacman import Pacman
from maze import Maze
from game_controller import GameController


def test_constructor():
    """Test Dots constructor"""
    ds = Dots(600, 600, 150, 450, 150, 450)
    assert ds.WIDTH == 600
    assert ds.HEIGHT == 600
    assert ds.TH == 150
    assert ds.BH == 450
    assert ds.LV == 150
    assert ds.RV == 450
    assert len(ds.bottom_row) == len(ds.top_row) == ds.WIDTH//ds.SPACING + 1
    assert len(ds.left_col) == len(ds.right_col) == ds.HEIGHT//ds.SPACING + 1
    for i in range(len(ds.left_col)):
        assert ds.left_col[i].x == ds.LV
        assert ds.left_col[i].y == ds.SPACING * i
    for i in range(len(ds.right_col)):
        assert ds.right_col[i].x == ds.RV
        assert ds.right_col[i].y == ds.SPACING * i
    for i in range(len(ds.top_row)):
        assert ds.top_row[i].x == ds.SPACING * i
        assert ds.top_row[i].y == ds.TH
    for i in range(len(ds.bottom_row)):
        assert ds.bottom_row[i].x == ds.SPACING * i
        assert ds.bottom_row[i].y == ds.BH


def test_eat():
    """ Test eat method """
    ds = Dots(600, 600, 150, 450, 150, 450)
    for x_coordinate in range(150, 451, 150):
        for y_coordinate in range(600):
            ds.eat(x_coordinate, y_coordinate)
    for y_coordinate in range(150, 451, 150):
        for x_coordinate in range(600):
            ds.eat(x_coordinate, y_coordinate)
    assert ds.dots_left() == 0


def test_dots_left():
    """ Test dots_left method"""
    ds = Dots(600, 600, 150, 450, 150, 450)
    dl = ds.dots_left()
    print(dl)
    assert dl == ((ds.WIDTH//ds.SPACING + 1) * 2 +
                  (ds.HEIGHT//ds.SPACING + 1) * 2)
