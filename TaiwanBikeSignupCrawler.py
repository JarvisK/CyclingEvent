import urllib.request
from bs4 import BeautifulSoup

class TaiwanBikeSignupCrawler():
    __targetURL = "http://www.taiwanbike.org/index.php/2012-01-17-13-13-47"
    __eventName = []
    __eventURL = []

    def startCrawler(self):
        with urllib.request.urlopen(self.__targetURL) as response:
            source = response.read()

            if source is None:
                raise ValueError("The source code is empty.")

            print("Processing " + self.__targetURL)

            self.parser(sourceCode=source)

        print("Taiwan bike signup complete")

    def parser(self, sourceCode=None):
        if sourceCode is None:
            raise ValueError("The source code is emtpy.")

        print("Processing " + self.__targetURL)

        soup = BeautifulSoup(sourceCode, "lxml")
        tableRow = soup.find('td', attrs={'class': 'article_indent'}).find_all('a')
        # tableRow = soup.find('table')
        for row in tableRow:
            self.__eventURL.append(row.attrs['href'])
            self.__eventName.append(row.find('span').text)
