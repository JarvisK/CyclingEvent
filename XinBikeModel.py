# -*- coding: utf-8 -*-
from MysqlConnector import MysqlConnector


class XinBikeModel(MysqlConnector):

    def __init__(self, crawler):
        self.crawler = crawler

    def insertAll(self):
        sql = ("INSERT INTO events (name, source_site, source_url, created_at, updated_at)"
               "VALUES (%s, %s, %s, now(), now())")

        for name, url in zip(self.crawler.eventName, self.crawler.eventURL):
            param = (name, "Xin Bike", url)
            self.query(sql, param)