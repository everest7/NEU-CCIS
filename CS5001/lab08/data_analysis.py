import re
import csv


class DataAnalysis:

    def __init__(self, file):
        # TODO: set up the necessary instance variables
        """ Initialize DataAnalysis with file_name, two dictionary storing
        languuage and domain respectively and user_number to store the number
        of users

        Args:
            file: the file_name will be set to
        """
        self.file_name = file
        self.languages = {}
        self.domains = {}
        self.user_number = 0

    def read_data(self, file_name):
        # TODO: read the data and get the counts
        """Count how many times each language shows up in a data item,
        and how many times each 2-letter country top-level domain signifier
        shows up in an email address.

        Args:
            file_name: file needs to be processed
        """
        with open(file_name, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)  # Skip the first line
            for line in csv_reader:
                self.user_number += 1
                if line[6] not in self.languages:
                    self.languages[line[6]] = 0
                self.languages[line[6]] += 1
                # Find all characters in a email address after '@' character
                # and identify top level domains as match[1]
                matches = re.findall(r'(@[\w._-]+\.(\w+))', line[3])
                for match in matches:
                    if (len(match[1]) <= 2):
                        if (match[1]) not in self.domains:
                            self.domains[match[1]] = 0
                        self.domains[match[1]] += 1

    # TODO:
    # Implement top_n_lang_freqs()
    # Should take a number N as an argument and return
    # an N-length list of tuples representing languages
    # and their frequencies in the data, ordered from
    # highest frequency to lowest.

    def top_n_lang_freqs(self, nth):
        """ Rank the frequency of language in a descending order

        Args:
            nth: representing the length of return list

        Returns:
            A dictionary of top n language frequency
        """
        total_n_langs = sum(self.languages.values())
        lang_freqs = {}
        for key, value in self.languages.items():
            lang_freqs[key] = value / total_n_langs
        top_n_lang_freq = sorted(lang_freqs.items(), key=lambda x: x[1],
                                 reverse=True)[:nth]
        return top_n_lang_freq

    # TODO:
    # Implement top_n_country_tlds_freqs()
    # Should take a number N as an argument and return
    # an N-length list of tuples representing country (2-letter)
    # top-level domain identifiers (e.g. 'jp', 'uk', 'cn', 'ca')
    # and their frequencies as email domains the data, ordered
    # from highest frequency to lowest.
    def top_n_country_tlds_freqs(self, nth):
        """ Rank the frequency of top level country domain in a descending order

        Args:
            nth: representing the length of return dictionary

        Returns:
            A dictionary of top n top level country domain
        """
        total_country_tlds = sum(self.domains.values())
        tlds_freq = {}
        for key, value in self.domains.items():
            tlds_freq[key] = value / self.user_number
        top_n_tlds_freq = sorted(tlds_freq.items(), key=lambda x: x[1],
                                 reverse=True)[:nth]
        return top_n_tlds_freq

    # TODO:
    # Implement any other necessary/helpful methods to support
    # the ones above.
