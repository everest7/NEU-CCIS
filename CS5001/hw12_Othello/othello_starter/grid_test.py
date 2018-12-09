from grid import Grid


def test_constructor():
    """Test Grid constructor"""
    grid = Grid(100, 100, 20)
    assert grid.WIDTH == 100
    assert grid.HEIGHT == 100
    assert grid.SPACING == 20
