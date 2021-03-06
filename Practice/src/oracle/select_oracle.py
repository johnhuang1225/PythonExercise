# coding=utf-8
import cx_Oracle


def get_local_oracle_connectin():
    """取得localhost oracle connection"""
    # con = cx_Oracle.connect('agentflow', 'agentflow', 'localhost:1521/A0801')
    con = cx_Oracle.connect('agentflow', 'agentflow', 'localhost:1521/a0801c.chenbro.com.tw')
    return con


def read_from_oracle():  
    con = get_local_oracle_connectin()
    cursor = con.cursor()
    cursor.execute(""" SELECT * FROM python_test """)
    template1 = 'memid:{0} , loginid:{1} , username:{2}'  # @UnusedVariable
    template2 = 'memid={memid} , loginid={loginid} , username={username}'
    all = cursor.fetchall()
    for row in all:
        # print(template1.format(row[0], row[1], row[2]))
        print(template2.format(memid=row[0], loginid=row[1], username=row[2]))
    cursor.close()
    con.commit()
    con.close()
    print('read_from_oracle ok')


read_from_oracle()
