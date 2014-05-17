# coding=utf-8
'''
Created on 2014/4/20

@author: john
'''
import csv

def get_csv(file_name):
    with open(file_name) as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        i = 0
        for row in f_csv:
            for j in range(len(headers)):
                message = '第{0}列的{1}是:{2}'.format((i + 1), headers[j], row[j])
                print(message, end='\t')
            i += 1    
            print('')

def get_cvs2(file_name, my_encoding='UTF-8'):
    with open(file_name, 'rt', encoding=my_encoding) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            print(', '.join(row))

get_cvs2('stocks.csv')
print('-' * 80)         
get_cvs2('stocks_big5.csv', 'Big5')          
            
