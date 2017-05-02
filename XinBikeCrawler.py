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
        tableRow = soup.find_all('p')
        for subRow in tableRow:
            target_dom = subRow.find('a', attrs={'target': '_blank'})
            if target_dom is None:
                continue
            else:
                self.__eventURL.append('http:' + str(target_dom.attrs['href']))
                self.__eventName.append(target_dom.text)

        print(len(self.__eventURL))
        print(len(self.__eventName))
