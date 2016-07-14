# coding=utf-8
import cx_Oracle

con = cx_Oracle.connect('agentflow', 'agentflow', 'localhost:1521/a0801c.chenbro.com.tw')
# print(con.version)
cursor = con.cursor()
sql = """ select * from mem_geninf where loginid='administrator'"""
cursor.execute(sql)
result = cursor.fetchall()
for row in result:
    print(row)
cursor.close()
con.close()


