import sys
from ngramfrequencies import NgramFrequencies
from textcleaner import TextCleaner
from nltk.tokenize import sent_tokenize


file_name = sys.argv[1]
unigram = NgramFrequencies('unigram')
bigram = NgramFrequencies('bigram')
trigram = NgramFrequencies('trigram')
text_Processor = TextCleaner()

try:
    with open(file_name, 'r') as file1:
        for line in file1.readlines():
            sentence = text_Processor.text_process(line)
            print(sentence)
            if len(sentence) != 0:
                for word_list in sentence:
                    word_list = word_list.split()
                    for word in word_list:
                        unigram.add_item(word)
                    for i in range(len(word_list) - 1):
                        bigram.add_item(word_list[i] + '_' + word_list[i + 1])
                    for i in range(len(word_list) - 2):
                        trigram.add_item(word_list[i] + '_' +
                                         word_list[i + 1] +
                                         '_' + word_list[i + 2])

        unigram.top_n_freqs()
        bigram.top_n_freqs()
        trigram.top_n_freqs()
except FileNotFoundError:
    print('File not found.')
