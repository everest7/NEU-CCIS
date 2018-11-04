from ngramfrequencies import NgramFrequencies
from textcleaner import TextCleaner


def test_ngram_constructor():
    """Test the NgramFrequencies constructor"""
    name = 'contructor'
    ngram = NgramFrequencies(name)
    assert ngram.name == name
    assert len(ngram.ngrams) == 0


def test_add_item():
    """Test add item function"""
    ngram = NgramFrequencies('ngram')
    key = 'word'
    ngram.add_item(key)
    assert ngram.ngrams[key] == 1


def test_top_n_counts():
    """Test top_n_counts function"""
    ngram = NgramFrequencies('ngram')
    textcleaner = TextCleaner()
    test_string = "Hello hello hello python python. This is a string to test\
    the top n counts function"
    process_text = textcleaner.text_process(test_string)
    for word_list in process_text:
        for word in word_list.split():
            ngram.add_item(word)
    top_10 = sorted(ngram.ngrams.items(), key=lambda x: x[1],
                    reverse=True)[:10]
    top_10_exp = [('hello', 3), ('python', 2), ('this', 1),
                  ('is', 1), ('a', 1), ('string', 1), ('to', 1),
                  ('test', 1), ('the', 1), ('top', 1)]
    assert top_10_exp == top_10


def test_top_n_freqs():
    """Test top_n_freqs function"""
    ngram = NgramFrequencies('ngram')
    textcleaner = TextCleaner()
    test_string = "A necro- philiac entertainment for the whole family to\
enjoy, \"Tim Burton's Corpse Bride\" marks the director's latest \
venture into the world of stop-motion animation"
    process_text = textcleaner.text_process(test_string)
    for word_list in process_text:
        for word in word_list.split():
            ngram.add_item(word)
    total_n_grams = sum(ngram.ngrams.values())
    word_freq = {}
    for key, value in ngram.ngrams.items():
        word_freq[key] = round(value / total_n_grams, 3)
    top_10_freq = sorted(word_freq.items(), key=lambda x: x[1],
                         reverse=True)[:10]
    top_10_freq_exp = [('the', 0.12), ('a', 0.04), ('necro', 0.04),
                       ('philiac', 0.04), ('entertainment', 0.04),
                       ('for', 0.04), ('whole', 0.04), ('family', 0.04),
                       ('toenjoy', 0.04), ('COMMA', 0.04)]
    assert top_10_freq == top_10_freq_exp


def test_frequency():
    """Test frequency function"""
    ngram = NgramFrequencies('ngram')
    textcleaner = TextCleaner()
    test_string = "Hello, world. Hello, Python"
    process_text = textcleaner.text_process(test_string)
    for word_list in process_text:
        for word in word_list.split():
            ngram.add_item(word)
    assert ngram.ngrams['hello'] == 2
