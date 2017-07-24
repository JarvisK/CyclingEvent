from TaiwanBikeNewsCrawler import TaiwanBikeNewsCrawler
from TaiwanBikeSignupCrawler import TaiwanBikeSignupCrawler
from TaiwanCyclistCrawler import TaiwanCyclistCrawler
from XinBikeCrawler import XinBikeCrawler

def main():
    a = XinBikeCrawler()
    a.startCrawler()
    a.fillData()

    b = TaiwanBikeNewsCrawler()
    b.startCrawler()
    b.fillData()

    c = TaiwanBikeSignupCrawler()
    c.startCrawler()
    c.fillData()

    d = TaiwanCyclistCrawler()
    d.startCrawler()
    d.fillData()

if __name__ == "__main__":
    main()
