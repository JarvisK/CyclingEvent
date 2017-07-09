import urllib.request
from bs4 import BeautifulSoup


class TaiwanBikeNewsCrawler():
    domainURL = "http://www.taiwanbike.org"
    __targetURL = "http://www.taiwanbike.org/index.php/2009-01-20-17-17-03"
    pageSeparator = 0
    __eventName = []
    __eventURL = []

    def startCrawler(self):
        morePages = True
        fetchURL = self.__targetURL

        while (morePages):
            with urllib.request.urlopen(fetchURL) as response:
                source = response.read()  # Get response source code

                if source is None:
                    raise ValueError("The source code is empty.")

                print("Processing " + self.__targetURL + "?start=" + str(self.pageSeparator))

                if (not self.parser(sourceCode=source)):
                    morePages = False
                else:
                    fetchURL = self.__targetURL + "?start=" + str(self.pageSeparator)
                    self.pageSeparator += 20

        print("Taiwan bike news complete.")

    def parser(self, sourceCode=None):
        if sourceCode is None:
            raise ValueError("The source code is empty.")

        soup = BeautifulSoup(sourceCode, "lxml")
        try:
            tableRow = soup.find('form', attrs={'name': 'adminForm'}).find('table').find_all('tr')
        except:
            return False

        for i, row in enumerate(tableRow):
            if 2 < i < 23:
                try:
                    self.__eventName.append(str(row.find('a').text).strip('\t\n\r'))
                    self.__eventURL.append(self.domainURL + str(row.find('a').attrs['href']).strip('\t\n\r'))
                except:
                    return False

        return True
