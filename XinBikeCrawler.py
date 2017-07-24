# -*- coding: utf-8 -*-
import urllib.request
from XinBikeModel import XinBikeModel
from bs4 import BeautifulSoup

class XinBikeCrawler:

    def __init__(self):
        self.targetURL = "http://solomo.xinmedia.com/bike/events?style=text"
        self.eventName = []
        self.eventURL = []

    def startCrawler(self):
        with urllib.request.urlopen(self.targetURL) as response:
            source = response.read()

            if source is None:
                raise ValueError("The source code is empty.")

            print("Processing " + self.targetURL)
            self.parser(sourceCode=source)
            print("Xinbike complete")

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
                self.eventURL.append('http:' + str(target_dom.attrs['href']))
                self.eventName.append(target_dom.text)

    def fillData(self):
        if len(self.eventName) == 0 or len(self.eventURL) == 0:
            return

        model = XinBikeModel(self)
        model.insertAll()