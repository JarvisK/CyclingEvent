# -*- coding: utf-8 -*-
import urllib.request
from TaiwanBikeSignupModel import TaiwanBikeSignupModel
from bs4 import BeautifulSoup

class TaiwanBikeSignupCrawler():

    def __init__(self):
        self.targetURL = "http://www.taiwanbike.org/index.php/2012-01-17-13-13-47"
        self.eventName = []
        self.eventURL = []

    def startCrawler(self):
        with urllib.request.urlopen(self.targetURL) as response:
            source = response.read()

            if source is None:
                raise ValueError("The source code is empty.")

            self.parser(sourceCode=source)

        print("Taiwan bike signup complete")

    def parser(self, sourceCode=None):
        if sourceCode is None:
            raise ValueError("The source code is empty.")

        print("Processing " + self.targetURL)

        soup = BeautifulSoup(sourceCode, "lxml")
        block = soup.find_all('p', attrs={'style': 'font-size: 12.16px; line-height: 15.808px;'})

        for content in block:
            main_tag = content.find("a", attrs={"rel": "noopener noreferrer"})
            if main_tag is None:
                continue

            name = main_tag.find('span')
            if name is None:
                name = main_tag.text
            else:
                name = name.text
            self.eventURL.append(main_tag.attrs['href'])
            self.eventName.append(name)

    def fillData(self):
        # Check data existence
        if len(self.eventName) == 0 or len(self.eventURL) == 0:
            return

        # Insert data
        model = TaiwanBikeSignupModel(self)
        model.insertAll()