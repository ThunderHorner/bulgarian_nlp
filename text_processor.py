from nltk.corpus import stopwords
from nltk import FreqDist


class TextProcessor():
    def __init__(self, filename, language='english'):
        self.stopwords = stopwords.words(language)
        self.filename = filename
        self.data = self.read_file()
        self.tokens = self.data.split()
        self.freq = FreqDist(self.tokens)

    def read_file(self):
        with open(self.filename) as file:
            return file.read()
