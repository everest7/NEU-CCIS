from tile import Tile


def test_constructor():
    """Test Tile constructor"""
    tile = Tile()
    assert tile.black_tile == 2
    assert tile.white_tile == 2
    assert tile.grid.WIDTH == 560
    assert tile.grid.HEIGHT == 560
    assert tile.grid.SPACING == 70
    assert len(tile.tile) == tile.grid.HEIGHT // tile.grid.SPACING
    assert len(tile.tile[0]) == tile.grid.WIDTH // tile.grid.SPACING


def test_check_legal_move():
    """Test check legal move method"""
    tile = Tile()
    assert tile.check_legal_move(0, 0) is False
    assert tile.check_legal_move(3, 2) is True


def test_ai_turn():
    """Test ai_turn method"""
    tile = Tile()
    tile.tile[3][5] = 1
    tile.counter = 2
    tile.ai_turn()
    assert tile.tile[3][3] == 2
    assert tile.tile[3][4] == 2
    assert tile.tile[3][5] == 2
    assert tile.tile[3][6] == 2


def test_record():
    """Test record method"""
    tile = Tile()
    tile.record("testname")
    test_index = "testname " + str(tile.black_tile)
    with open("Score.txt", 'r') as rf:
        lines = rf.readlines()
        score_file = [line.rstrip('\n') for line in lines]
    assert test_index in score_file
