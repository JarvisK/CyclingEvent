import urllib.request
from bs4 import BeautifulSoup

class TaiwanBikeCrawler():
    domainURL = "http://www.taiwanbike.org"
    targetURL = "http://www.taiwanbike.org/index.php/2009-01-20-17-17-03"

    def getHtmlSourceCode(self):
        with urllib.request.urlopen(self.targetURL) as response:
            self.sourceCode = response.read()
            self.parser()

    def parser(self):
        soup = BeautifulSoup(self.sourceCode, "lxml")
        tableRow = soup.find('form', attrs={'name':'adminForm'}).find('table').find_all('tr')

        eventName = []
        eventURL = []

        for i, row in enumerate(tableRow):
            if 3 < i < 23:
                eventName.append(str(row.contents[3].a.string).strip('\t\n\r'))
                eventURL.append(str(row.contents[3].a.attrs['href']).strip('\t\n\r'))

        print(eventURL)