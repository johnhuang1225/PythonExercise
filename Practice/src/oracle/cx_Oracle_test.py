# coding=utf-8
'''
Created on 2014/5/14

@author: John Huang
'''

import cx_Oracle

con = cx_Oracle.connect('agentflow','agentflow','localhost:1521/A0801')
# print(con.version)
cursor = con.cursor()
sql = """ select * from mem_geninf where loginid='a0801'"""
cursor.execute(sql)
result = cursor.fetchall()
for row in result:
    print(row)
cursor.close()
con.close()


