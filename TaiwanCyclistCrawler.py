# -*- coding: utf-8 -*-
import urllib.request
from TaiwanCyclistModel import TaiwanCyclistModel
from bs4 import BeautifulSoup

class TaiwanCyclistCrawler():

    def __init__(self):
        self.eventName = []
        self.eventURL = []
        self.eventStatus = []
        self.domainName = "http://www.cyclist.org.tw"
        self.targetURL = "http://www.cyclist.org.tw/eventnew.asp?page="

    def startCrawler(self):
        currentPage = 1
        morePages = True

        while(morePages):
            with urllib.request.urlopen(self.targetURL + str(currentPage)) as response:
                source = response.read()

                if source is None:
                    raise ValueError("The source code is empty.")

                print("Processing " + self.targetURL + str(currentPage))

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

        table_row = soup.find_all('div', attrs={'class': 'eventItem'})

        for row in table_row:
            status = row.find('span', attrs={'class': 'btn'}).text
            url = self.domainName + '/' + row.find('a', attrs={'class': 'btn'}).attrs['href']
            name = row.find('h3', attrs={'class': 'entry-title'}).text.strip()
            sub_name = row.find('div', attrs={'class': 'entry-meta'}).text.strip()

            self.eventName.append(name + sub_name)
            self.eventURL.append(url)
            self.eventStatus.append(status)

    def fillData(self):
        if len(self.eventName) == 0 or len(self.eventURL) == 0:
            return

        model = TaiwanCyclistModel(self)
        model.insertAll()