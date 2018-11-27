from word_ladder import WordLadder


# TODO: Write appropriate unit tests
def load_words():
    """Load words from complete wordlist file"""
    # We're creating a dictionary keyed on word
    # length, so that we can quickly get to a set of
    # words of a given length.
    valid_words = {}
    with open('words_alpha.txt') as word_file:
        for w in word_file.read().split():
            if len(w) in valid_words.keys():
                # Add to an existing set
                valid_words[len(w)].add(w)
            else:
                # Initialize a set with one element
                valid_words[len(w)] = {w}
    return valid_words


def test_make_ladder():
    english_words = load_words()
    w1, w2 = 'love', 'hate'
    wl = WordLadder(w1, w2, english_words[len(w1)])
    word_ladder = wl.make_ladder()
    expected = ['love', 'hove', 'have', 'hate']
    flag = True
    for i in reversed(range(len(expected))):
        if expected[i] != word_ladder.pop():
            flag = False
    assert flag
