import urllib.request
from bs4 import BeautifulSoup

class TaiwanCyclistCrawler():
    __domainName = 'http://www.cyclist.org.tw'
    __targetURL = 'http://www.cyclist.org.tw/eventnew.asp?page='
    __eventName = []
    __eventURL = []
    __eventStatus = []

    def startCrawler(self):
        currentPage = 1
        morePages = True

        while(morePages):
            with urllib.request.urlopen(self.__targetURL + str(currentPage)) as response:
                source = response.read()

                if source is None:
                    raise ValueError("The source code is empty.")

                print("Processing " + self.__targetURL + str(currentPage))

                bufySource = BeautifulSoup(source, "lxml")
                checkNextPage = bufySource.find('ul', attrs={'class': 'pagination'}).findAll('li')[1].find('a').attrs["href"]
                if checkNextPage == "#":
                    morePages = False
                else:
                    currentPage += 1

                self.parser(soup=bufySource)

        print("Taiwan cyclist complete.")

    def parser(self, soup):
        if soup is None:
            raise ValueError("The source code is emtpy.")

        tableRow = soup.findAll('div', attrs={'class': 'eventItem'})

        for row in tableRow:
            status = row.find('span', attrs={'class': 'btn'}).text
            url = self.__domainName + '/' + row.find('a', attrs={'class': 'btn'}).attrs['href']
            name = row.find('h3', attrs={'class': 'entry-title'}).text.strip()
            sub_name = row.find('div', attrs={'class': 'entry-meta'}).text.strip()

            self.__eventName.append(name + sub_name)
            self.__eventURL.append(url)
            self.__eventStatus.append(status)
