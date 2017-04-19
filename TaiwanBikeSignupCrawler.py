import urllib.request
from bs4 import BeautifulSoup

class TaiwanBikeSignupCrawler():
    targetURL = "http://www.taiwanbike.org/index.php/2012-01-17-13-13-47"
    eventName = []
    eventURL = []

    def startCrawler(self):
        with urllib.request.urlopen(self.targetURL) as response:
            source = response.read()

            if source is None:
                raise ValueError("The source code is empty.")

            self.parser(sourceCode=source)

    def parser(self, sourceCode=None):
        if sourceCode is None:
            raise ValueError("The source code is emtpy.")

        soup = BeautifulSoup(sourceCode, "lxml")
        tableRow = soup.find('td', attrs={'class': 'article_indent'}).find_all('a')
        # tableRow = soup.find('table')
        for row in tableRow:
            self.eventURL.append(row.attrs['href'])
            self.eventName.append(row.find('span').text)
