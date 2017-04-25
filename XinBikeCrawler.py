import urllib.request
from bs4 import BeautifulSoup

class XinBikeCrawler:
    __targetURL = "http://solomo.xinmedia.com/bike/events?style=text"
    __eventName = []
    __eventURL = []

    def startCrawler(self):
        with urllib.request.urlopen(self.__targetURL) as response:
            source = response.read()

            if source is None:
                raise ValueError("The source code is empty.")

            print("Processing " + self.__targetURL)

            self.parser(sourceCode=source)

    def parser(self, sourceCode=None):
        if sourceCode is None:
            raise ValueError("The source code is empty.")

        soup = BeautifulSoup(sourceCode, "lxml")
        tableRow = soup.find('div', attrs={'class': 'summary'})
