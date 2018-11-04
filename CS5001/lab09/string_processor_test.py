from string_processor import StringProcessor


def test_process_string():
    """Test for process_string function"""
    # Include the following cases
    # "ab" should yield "" as ouptut
    # "ab*" should yield "b" as output
    # "ab^" should yield "ba" as output
    # "^" should yield "" as output
    process_test = StringProcessor()
    assert process_test.process_string("ab") == ""
    assert process_test.process_string("ab*") == "b"
    assert process_test.process_string("ab^") == "ba"
    assert process_test.process_string("^") == ""
