# coding=utf-8
import csv
import cx_Oracle


def get_local_oracle_connectin():
    """取得localhost oracle connection"""
    # con = cx_Oracle.connect('xxxx', 'xxxx', 'xxx.xx.xx.xx:xxxx/xxx')
    con = cx_Oracle.connect('agentflow', 'agentflow', 'localhost:1521/a0801c.chenbro.com.tw')
    return con


def insert_header(file_name, default_encoding='UTF-8'):
    """insert to FLW_IP_HEADER table"""
    with open(file_name, 'r', encoding=default_encoding) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        con = get_local_oracle_connectin()
        param = []
        for row in csvreader:
            param.append((row[0].strip(), row[1].strip()))
        cursor = con.cursor()
        cursor.executemany("""
            insert into FLW_IP_HEADER(HEADER_ID, HEADER_NAME) values(:1, :2)
            """, param)
        cursor.close()
        con.commit();
        con.close()
        print(param)
        print('ok')


def insert_detail(file_name, default_encoding='UTF-8'):
    """insert to FLW_IP_DETAIL table"""
    with open(file_name, 'r', encoding=default_encoding) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        con = get_local_oracle_connectin()
        param = []
        for row in csvreader:
            param.append((row[0].strip(), row[1].strip(), row[2].strip()))
        cursor = con.cursor()
        cursor.executemany("""
            insert into FLW_IP_DETAIL(DETAIL_ID, HEADER_ID, DETAIL_NAME) values(:1, :2, :3)
            """, param)
        cursor.close()
        con.commit();
        con.close()
        print(param)
        print('ok')

# insert_header('ip/01-item_master.csv')

insert_detail('ip/02-item_detail.csv')











