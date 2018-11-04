import re


class TextCleaner:
    def __init__(self):
        pass

    def text_process(self, text):
        """Carry out the text pre-processing

        Args:
            text: text needs to be processed

        Returns:
            A list of words after processing
        """
        text = re.sub(r'((M(r|s|rs))(\.))', r'\2', text)
        text = text.rstrip()
        text = text.lower()
        text = text.replace(',', ' COMMA')
        text = text.replace('(', '')
        text = text.replace(')', '')
        text = text.replace('"', '')
        text = text.replace('-', '')
        sentence = text.split('.')
        return sentence
