class NgramFrequencies():
    def __init__(self, name):
        """Initialize NgramFrequencies with a name, and a dictionary storing
        ngrams"""
        self.name = name
        self.ngrams = {}

    def add_item(self, key):
        """Add item to the n_grams dictionary"""
        if (key not in self.ngrams):
            self.ngrams[key] = 0
        self.ngrams[key] += 1

    def top_n_counts(self):
        """Print a list of items sorted on the count, in a descending order"""
        top_10_count = sorted(self.ngrams.items(), key=lambda x: x[1],
                              reverse=True)[:10]
        print('Top 10 ' + self.name + ': ')
        for item in top_10_count:
            print(item)

    def top_n_freqs(self):
        """Print a list of items sorted on the frequency, in a descending
        order"""
        total_n_grams = sum(self.ngrams.values())
        word_freq = {}
        for key, value in self.ngrams.items():
            word_freq[key] = value / (total_n_grams)
        top_10_freq = sorted(word_freq.items(), key=lambda x: x[1],
                             reverse=True)[:10]
        print('Top 10 ' + self.name + ': ')
        for item in top_10_freq:
            print(item)

    def frequency(self, key):
        """Return the frequency of a specified n_gram"""
        return self.ngrams[key]
