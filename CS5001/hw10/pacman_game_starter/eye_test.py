from eye import Eye


def test_constructor():
    """Test Eye constructor"""
    e = Eye()
    assert e.direction == (0, 0)


def test_look():
    """Test look method"""
    e = Eye()
    e.look((1, 1))
    assert e.direction == (1, 1)
