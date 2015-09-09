# coding=utf-8
'''
Created on 2015/9/9

@author: John Huang
集保庫存crawler
'''
import requests
from bs4 import BeautifulSoup as BS
res = requests.get("http://www.tdcc.com.tw/smWeb/QryStock.jsp?SCA_DATE=20150807&SqlMethod=StockNo&StockNo=8114&StockName=&sub=%ACd%B8%DF")
soup = BS(res.text,"html.parser")
tb = soup.select('.mt')[1]
for tr in tb.select('tr'):
    print tr.select('td')[0].text, tr.select('td')[1].text, tr.select('td')[2].text, tr.select('td')[3].text, tr.select('td')[4].text