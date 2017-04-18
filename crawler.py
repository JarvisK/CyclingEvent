import urllib.request
from bs4 import BeautifulSoup


class TaiwanBikeCrawler():
    domainURL = "http://www.taiwanbike.org"
    targetURL = "http://www.taiwanbike.org/index.php/2009-01-20-17-17-03"
    pageSeparator = 20
    eventName = []
    eventURL = []

    def startCrawler(self):
        keep = True
        fetchURL = self.targetURL

        while (keep):
            with urllib.request.urlopen(fetchURL) as response:
                source = response.read()  # Get response source code

                if source is None:
                    raise ValueError("The source code is empty.")

                if (not self.parser(sourceCode=source)):
                    keep = False
                else:
                    fetchURL = self.targetURL + "?start=" + str(self.pageSeparator)
                    self.pageSeparator += 20

        print("Crawler success.")

    def parser(self, sourceCode=None):
        if sourceCode is None:
            raise ValueError("The source code is empty.")

        print("Processing " + self.targetURL + "...")

        soup = BeautifulSoup(sourceCode, "lxml")
        tableRow = soup.find('form', attrs={'name': 'adminForm'}).find('table').find_all('tr')

        if tableRow == None:
            return False

        for i, row in enumerate(tableRow):
            if 2 < i < 23:
                try:
                    self.eventName.append(str(row.contents[3].a.string).strip('\t\n\r'))
                    self.eventURL.append(self.domainURL + str(row.contents[3].a.attrs['href']).strip('\t\n\r'))
                except:
                    return False

        return True
