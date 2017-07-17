# -*- coding: utf-8 -*-
from MysqlConnector import MysqlConnector
from TaiwanBikeSignupCrawler import TaiwanBikeSignupCrawler

class TaiwanBikeSignupModel(MysqlConnector):
    __TBSC = None

    def __init__(self):
        super(TaiwanBikeSignupModel, self).__init__()
        self.__TBSC = TaiwanBikeSignupCrawler()
        self.__TBSC.startCrawler()
        self.update()

    def update(self):
        for name, url in zip(self.__TBSC.eventName, self.__TBSC.eventURL):
            sql = ("INSERT INTO events (name, source_site, source_url, created_at, updated_at)"
                    "VALUES (%s, %s, %s, now(), now())")

            param = (name, "Taiwan Bike", url)

            self.query(sql, param)

tbsm = TaiwanBikeSignupModel()
