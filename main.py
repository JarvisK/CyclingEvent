from TaiwanBikeNewsCrawler import TaiwanBikeNewsCrawler
from TaiwanBikeSignupCrawler import TaiwanBikeSignupCrawler

def main():
    a = TaiwanBikeSignupCrawler()
    a.startCrawler()
    print(a.eventURL)
    # http://bao-ming.com/eb/www/reg.php?activitysn=2048

if __name__ == "__main__":
    main()
