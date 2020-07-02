from nltk.corpus import stopwords
from nltk import FreqDist
import urllib.request

from settings import STOPWORDS
from bs4 import BeautifulSoup


class TextProcessor():
    def __init__(self, language='english', url=None, filename=None):
        self.url = url
        self.filename = filename
        if filename is None and url is None \
                or filename is not None and url is not None:
            raise AttributeError('You must specify either url or filename')
        if filename is not None:
            self.data = self.read_file()
        if url is not None:
            self.data = self.proceed_url()

        self.stopwords = STOPWORDS

        self.tokens = [token for token in  self.data.split() if token not in self.stopwords]
        self.freq = FreqDist(self.tokens)
        self.context = list(self.freq)[0]

    def read_file(self):
        with open(self.filename) as file:
            return file.read()

    def proceed_url(self):
        response = urllib.request.urlopen(self.url)
        html = response.read()
        soup = BeautifulSoup(html)
        text = soup.find('div', {"class":"news"}).get_text(strip=True)

        return text

