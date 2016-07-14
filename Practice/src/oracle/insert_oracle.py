# coding=utf-8
import csv
import cx_Oracle


def get_local_oracle_connectin():
    """取得localhost oracle connection"""
    # con = cx_Oracle.connect('agentflow', 'agentflow', 'localhost:1521/A0801')
    con = cx_Oracle.connect('agentflow', 'agentflow', 'localhost:1521/a0801c.chenbro.com.tw')
    return con


def read_csv_2_oracle(file_name, default_encoding='UTF-8'):
    with open(file_name, 'rt', encoding=default_encoding) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        con = get_local_oracle_connectin()
        for row in csvreader:
            multi_insert_param(con, row)  
        con.commit()
        con.close()        
        print('read_csv() ok')
        

def multi_insert_param(con, data):
    param = [{'memid':data[0], 'loginid':data[1], 'username':data[2]}]
    sql = """ insert into PYTHON_TEST values(:memid,:loginid,:username) """
    cursor = con.cursor()
    cursor.executemany(sql, param)
    cursor.close()
            

def single_insert(con):
    """insert一筆資料"""
    cursor = con.cursor()
    cursor.execute("insert into PYTHON_TEST values('1','johnhuang','黃獻葦')")
    cursor.close()
    con.commit()
    con.close()
    print('single_insert() ok')


def single_insert_param(con):
    cursor = con.cursor()
    param = {'memid':'param_insert', 'loginid':'param_insert', 'username':'param_insert'}
    sql = """ insert into PYTHON_TEST values(:memid,:loginid,:username) """
    cursor.execute(sql, param)
    cursor.close()
    con.commit()
    con.close()
    print('single_insert_param() ok')
    

def multi_insert_param2(con):
    param = []
    for i in range(1, 10):
        param.append((str(i), 'memid' + str(i), 'username' + str(i)))
    cursor = con.cursor()
    cursor.executemany(""" insert into PYTHON_TEST values(:1,:2,:3) """, param)
    cursor.close()
    con.commit()
    con.close()
    print('multi_insert_param2(con) ok')


def insert_cycle(file_name, default_encoding='UTF-8'):
    """直接讀取csv檔，insert to oracle"""
    with open(file_name,'r',encoding=default_encoding) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        con = get_local_oracle_connectin()
        param = []
        for row in csvreader:
            param.append((row[0],row[1],row[2]))
        cursor = con.cursor()
        cursor.executemany(""" insert into PYTHON_TEST values(:1,:2,:3) """, param)
        cursor.close()
        con.commit();
        con.close()
        print(param)
        print('insert_cycle ok')


"""5"""
# insert_cycle('insert_data.csv')


"""4"""
con = get_local_oracle_connectin()
multi_insert_param2(con)


"""3"""
# con = get_local_oracle_connectin()    
# single_insert_param(con)

"""2"""
# read_csv_2_oracle('insert_data.csv')  

"""1"""
# con = get_local_oracle_connectin()
# single_insert(con)




