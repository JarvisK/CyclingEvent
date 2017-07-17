# -*- coding: utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup

class TaiwanBikeSignupCrawler():
    __targetURL = "http://www.taiwanbike.org/index.php/2012-01-17-13-13-47"
    eventName = []
    eventURL = []

    def startCrawler(self):
        with urllib.request.urlopen(self.__targetURL) as response:
            source = response.read()

            if source is None:
                raise ValueError("The source code is empty.")

            self.parser(sourceCode=source)

        print("Taiwan bike signup complete")

    def parser(self, sourceCode=None):
        if sourceCode is None:
            raise ValueError("The source code is empty.")

        print("Processing " + self.__targetURL)

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
