from game_controller import GameController


def test_constructor():
    """Test Game_Controller constructor"""
    gc = GameController(500, 300)
    assert gc.WIDTH == 500
    assert gc.HEIGHT == 300
    assert gc.player_wins is False
    assert gc.pinky_wins is False
