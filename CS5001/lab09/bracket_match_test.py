from bracket_match import BracketMatch


def test_brackets_match():
    """Test brackets_match method"""
    # Include the following cases in your test:
    # "()" should succeed
    # "a(a[a])a({a})" should succeed
    # "(" should not succeed
    # "(}" should not succeed
    # "a(a(a)a(a)" should not succeed
    # "aa(a))a(a)" should not succeed
    bracket_test = BracketMatch()
    assert bracket_test.brackets_match('()') is True
    assert bracket_test.brackets_match('a(a[a])a({a})') is True
    assert bracket_test.brackets_match('(') is False
    assert bracket_test.brackets_match('(}') is False
    assert bracket_test.brackets_match('a(a(a)a(a)') is False
    assert bracket_test.brackets_match('aa(a))a(a)') is False


test_brackets_match()
