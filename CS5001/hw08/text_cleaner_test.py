from textcleaner import TextCleaner


def test_text_process():
    """Test the text_process function"""
    textcleaner = TextCleaner()
    test_string = "A necro- philiac entertainment for the whole family to\
enjoy, \"Tim Burton's Corpse Bride\" marks the director's latest \
venture into the world of stop-motion animation"
    processed_text = textcleaner.text_process(test_string)
    flag = True
    for word_list in processed_text:
        for word in word_list:
            if '()-"\'' in word:
                flag = False
    assert flag
