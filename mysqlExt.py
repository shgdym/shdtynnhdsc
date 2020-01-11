#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pymysql
from const import const

__author__ = 'shgdym'

class MySql:
    def __init__(self, host=const.DB_HOST, user=const.DB_USER, password=const.DB_PASS, db=const.DB_NAME, port=const.DB_PORT):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.port = port
        self.connect()

    def connect(self):
        """
        :connect to mysql
        """
        if 'cursor' in locals().keys():
            pass
        else:
            self.dbconn = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db, port=self.port)
            self.cursor = self.dbconn.cursor()

    def getRows(self, query_sql):
        """
        :param query_sql:
        :return: query result
        """
        self.cursor.execute(query_sql)
        results = self.cursor.fetchall()
        return results

    def getFirstRow(self, query_sql):
        """
        :param query_sql:
        :return: first row of query result
        """
        res = self.getRows(query_sql)
        if len(res) == 0:
            return ""
        return res[0]

    def getFirstRowColumn(self, query_sql):
        """
        :param query_sql:
        :return: first row column of query result
        """
        row = self.getFirstRow(query_sql)
        if row == "":
            return ""
        return row[0]

    def query(self, query_sql):
        """
        :param query_sql:
        :return: boole
        """
        self.cursor.execute(query_sql)
        r = self.dbconn.commit()

    def close(self):
        """
        :close mysql connect
        """
        self.cursor.close()