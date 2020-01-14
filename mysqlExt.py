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
        if 'cursor' in locals().keys():
            pass
        else:
            self.dbconn = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db, port=self.port, charset='utf8mb4')
            self.cursor = self.dbconn.cursor()

    def getRows(self, query_sql):
        self.cursor.execute(query_sql)
        results = self.cursor.fetchall()
        return results

    def getFirstRow(self, query_sql):
        res = self.getRows(query_sql)
        if len(res) == 0:
            return ""
        return res[0]

    def getFirstRowColumn(self, query_sql):
        row = self.getFirstRow(query_sql)
        if row == "":
            return ""
        return row[0]

    def query(self, query_sql):
        self.cursor.execute(query_sql)
        self.dbconn.commit()

    def close(self):
        self.cursor.close()

# if __name__ == "__main__":
#     objMysql = MySqlExt()
#     # sql = """CREATE TABLE EMPLOYEE (
#     #          FIRST_NAME  CHAR(20) NOT NULL,
#     #          LAST_NAME  CHAR(20),
#     #          AGE INT,
#     #          SEX CHAR(1),
#     #          INCOME FLOAT )"""
#     # objMysql.query(sql)
#     #
#     # sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
#     #          LAST_NAME, AGE, SEX, INCOME)
#     #          VALUES ('Mac', 'Mohan', 20, 'M', 2000),('john', 'Mohan', 22, 'W', 1000)"""
#     # objMysql.query(sql)
#
#     sql = """SELECT age
#              FROM EMPLOYEE
#              where age >55"""
#     res = objMysql.getFirstRowColumn(sql)
#     print(res)
#     exit()
