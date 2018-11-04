import sys
from data_analysis import DataAnalysis


def main(file_name):
    data = DataAnalysis(file_name)
    data.read_data(file_name)

    # Report top ten languages by frequency
    print("Languages:")
    data.top_n_lang_freqs(10)
    print_output(data.top_n_lang_freqs(10))

    # Report top ten country (2 letter) top
    # level domains by frequency
    print("Top level country domains:")
    print_output(data.top_n_country_tlds_freqs(10))


def print_output(collection):
    for item in collection:
        print(item[0]+":  \t", round(item[1], 3))


main(sys.argv[1])
