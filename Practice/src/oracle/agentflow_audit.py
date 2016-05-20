# coding=utf-8
'''
Created on 2016/5/20

@author: John Huang
'''

import csv, cx_Oracle

"""取得localhost oracle connection"""
def get_local_oracle_connectin():
    con = cx_Oracle.connect('agentflow', 'agentflow', 'localhost:1521/A0801')
    return con



"""insert to audit_cycle table"""
def insert_cycle(file_name, default_encoding='UTF-8'):
    with open(file_name,'r', encoding=default_encoding) as csvfile:
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


"""insert to insert_operation table"""
def insert_operation(file_name, default_encoding='UTF-8'):
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


"""insert to insert_matter table"""
def insert_matter(file_name, default_encoding='UTF-8'):
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


# insert_cycle('01.cycle.csv')
# insert_operation('02.operation.csv')

insert_matter('03.matter.csv')










