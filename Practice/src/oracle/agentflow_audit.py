# coding=utf-8
import csv
import cx_Oracle


def get_local_oracle_connectin():
    """取得localhost oracle connection"""
    # con = cx_Oracle.connect('xxxx', 'xxxx', 'xxx.xx.xx.xx:xxxx/xxx')
    con = cx_Oracle.connect('agentflow', 'agentflow', 'localhost:1521/a0801c.chenbro.com.tw')
    return con


def insert_cycle(file_name, default_encoding='UTF-8'):
    """insert to audit_cycle table"""
    with open(file_name, 'r', encoding=default_encoding) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        con = get_local_oracle_connectin()
        param = []
        for row in csvreader:
            param.append((row[0].strip(), row[1].strip()))
        cursor = con.cursor()
        cursor.executemany(""" 
            insert into audit_cycle(cycle_id, cycle_name) values(:1, :2) 
            """, param)
        cursor.close()
        con.commit();
        con.close()
        print(param)
        print('ok')


def insert_operation(file_name, default_encoding='UTF-8'):
    """insert to insert_operation table"""
    with open(file_name, 'r', encoding=default_encoding) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        con = get_local_oracle_connectin()
        param = []
        for row in csvreader:
            param.append((row[0].strip(), row[1].strip(), row[2].strip()))
        cursor = con.cursor()
        cursor.executemany(""" 
            insert into audit_operation(operation_id, cycle_id, operation_name) values(:1, :2, :3) 
            """, param)
        cursor.close()
        con.commit();
        con.close()
        print(param)
        print('ok')


def insert_matter_each(file_name, default_encoding='UTF-8'):
    """insert to insert_matter table"""
    with open(file_name, 'r', encoding=default_encoding) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        con = get_local_oracle_connectin()
        param = []
        for row in csvreader:
            param.append((row[0].strip(), row[1].strip(), row[2].strip()))
        cursor = con.cursor()
        cursor.executemany(""" 
            insert into audit_matter(cycle_id, operation_id, matter_name) values(:1, :2, :3) 
            """, param)
        cursor.close()
        con.commit();
        con.close()
        print(param)
        print('ok')


def insert_matter():
    items = [
             '03.matter-01-AS.csv',  # ok
             '03.matter-02-AP.csv',  # ok
             '03.matter-03-AO.csv',  # ok
             '03.matter-04-AW.csv',  # ok
             '03.matter-05-AR.csv',  # ok
             '03.matter-06-AF.csv',  # ok
             '03.matter-07-AI.csv',  # ok
             '03.matter-08-AD.csv',  # ok
             '03.matter-09-AC.csv',  # ok
             '03.matter-10-AM.csv'  # ok
             ]
    for item in items:
        insert_matter_each('audit/' + item)

# insert_cycle('audit/01.cycle.csv')

# insert_operation('audit/02.operation.csv')

# insert_matter()










