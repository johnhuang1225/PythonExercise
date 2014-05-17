# coding=utf-8
'''
Created on 2014/4/20

@author: john
'''
import collections

Sale = collections.namedtuple('Sale', 'productid customername date quantity price')
sales = []
sales.append(Sale('001', '鴻海', '2014/01/01', 500, 10))
sales.append(Sale('002', '正崴', '2014/02/01', 200, 30))

total = 0
for sale in sales:
    sub = sale.quantity * sale.price
    print('第1種格式化 - 代號:{0},名稱:{1},金額:{2}'.format(sale.productid, sale.customername, sub))
    print('第2種格式化 - 代號:{0.productid},名稱:{0.customername},金額:{1}'.format(sale, sub))
    print('第3種格式化 - 代號:{productid},名稱:{customername}'.format(**sale._asdict()))
    print('=' * 20)
    total += sub

print('所有金額:{0}'.format(total))
    

