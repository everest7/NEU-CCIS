from tile import Tile
from computer import Computer


def test_constructor():
    """Test constructor"""
    tile = Tile()
    computer = Computer(tile)
    assert computer.ai_turn is False
    assert computer.player_turn is False
    assert computer.ai_legal_moves == []
    assert computer.player_legal_moves == []
    assert computer.tile == tile
    assert computer.best_move == [0, 0]


def test_all_legal_moves():
    """Test all_legal_moves method.
    When the game is initialized, there are four legal moves
    for either black or white tile"""
    tile = Tile()
    computer = Computer(tile)
    legal_move = computer.all_legal_moves()
    assert legal_move == [(2, 3), (3, 2), (4, 5), (5, 4)]


def test_ai_make_move():
    """Test ai_make_move method. Make sure the move has
    been made and tiles in between have been flipped"""
    tile = Tile()
    tile.tile = [[0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 2, 1, 0, 0, 0],
                 [0, 0, 1, 1, 2, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0]]
    tile.counter = 2
    computer = Computer(tile)
    lm = computer.all_legal_moves()
    computer.ai_make_move()
    assert (tile.tile[4][1] == 2) and (
        tile.tile[4][2] == 2) and (tile.tile[4][3] == 2)
