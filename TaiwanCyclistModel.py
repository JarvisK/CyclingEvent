# -*- coding: utf-8 -*-
from MysqlConnector import MysqlConnector

class TaiwanCyclistModel(MysqlConnector):

    def __init__(self, crawler):
        self.crawler = crawler

    def insertAll(self):
        for name, url in zip(self.crawler.eventName, self.crawler.eventURL):
            sql = ("INSERT INTO events (name, source_site, source_url, created_at, updated_at)"
                   "VALUES (%s, %s, %s, now(), now())")

            param = (name, "Taiwan Cyclist", url)
            self.query(sql, param)