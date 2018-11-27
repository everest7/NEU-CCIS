from word_ladder import WordLadder


def main():
    """Run an interactive command line to let the user
    input word pairs and generate word ladders"""
    english_words = load_words()
    # print(english_words[len('hel')])
    while True:
        w1, w2 = input("> ").split()
        # Create a WordLadder object
        if len(w1) < len(w2):
            vary_length_words = {w1}
            for i in range(len(w1), len(w2) + 1):
                vary_length_words = vary_length_words | english_words[i]
        elif len(w1) > len(w2):
            vary_length_words = {w2}
            for i in range(len(w2), len(w1) + 1):
                vary_length_words = vary_length_words | english_words[i]
        else:
            vary_length_words = english_words[len(w1)]
        wl = WordLadder(w1, w2, vary_length_words)
        # Generate the word ladder
        word_ladder = wl.make_ladder()
        print("Ladder: ", word_ladder)


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

main()
