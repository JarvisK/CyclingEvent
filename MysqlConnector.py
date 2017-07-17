# -*- coding: utf-8 -*-
""" DocString
This is mysql connector.
"""
import mysql.connector

class MysqlConnector:
    __host = 'localhost'
    __user = 'root'
    __pwd = 'a97222037'
    __db = 'cycling_event'

    def __open(self):
        self.__cnx = mysql.connector.connect(
            user=self.__user,
            password=self.__pwd,
            host=self.__host,
            database=self.__db
        )
        self.__cursor = self.__cnx.cursor()

    def __close(self):
        self.__cursor.close()
        self.__cnx.close()

    def query(self, sql, param):
        self.__open()
        self.__cursor.execute(sql, param)
        self.__cnx.commit()
        self.__close()
