# coding=utf-8
'''
Created on 2015/9/9

@author: John Huang
'''
import requests
from bs4 import BeautifulSoup

res = requests.get('http://tw.taobao.com/product/%E5%A4%9A%E6%A8%A3%E5%B1%8B-%E8%91%AB%E8%98%86-%E4%BF%9D%E6%BA%AB%E6%9D%AF.htm')
soup = BeautifulSoup(res.text)
for item in soup.select('.item'):
    print(item.select('strong')[0].text), item.select('.title')[0].text.strip()