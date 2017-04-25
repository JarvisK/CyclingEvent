from TaiwanBikeNewsCrawler import TaiwanBikeNewsCrawler
from TaiwanBikeSignupCrawler import TaiwanBikeSignupCrawler
from TaiwanCyclistCrawler import TaiwanCyclistCrawler
from XinBikeCrawler import XinBikeCrawler

def main():
    # a = TaiwanBikeSignupCrawler()
    # a.startCrawler()
    # b = TaiwanBikeNewsCrawler()
    # b.startCrawler()
    # c = TaiwanCyclistCrawler()
    # c.startCrawler()
    d = XinBikeCrawler()
    d.startCrawler()
    # http://bao-ming.com/eb/www/reg.php?activitysn=2048

if __name__ == "__main__":
    main()
