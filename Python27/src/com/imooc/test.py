# coding=utf-8
'''
Created on 2015/8/15

@author: John Huang
'''
# import requests
# from bs4 import BeautifulSoup as BS
# res = requests.get("http://www.tdcc.com.tw/smWeb/QryStock.jsp?SCA_DATE=20150807&SqlMethod=StockNo&StockNo=8114&StockName=&sub=%ACd%B8%DF")
# soup = BS(res.text,"html.parser")
# tb = soup.select('.mt')[1]
# for tr in tb.select('tr'):
#     print tr.select('td')[0].text, tr.select('td')[1].text, tr.select('td')[2].text, tr.select('td')[3].text, tr.select('td')[4].text


from bs4 import BeautifulSoup
html_sample = '\
<!DOCTYPE html>\
<html lang="en">\
<head>\
    <meta charset="UTF-8">\
    <title>Document</title>\
</head>\
<body>\
    <h1 id="title">Hello World</h1>\
    <h1 id="test">Python</h1>\
    <a href="#" class="link">This is link1</a>\
    <a href="#" class="link">This is link2</a>\
</body>\
</html>\
'
soup = BeautifulSoup(html_sample)
print(soup.select('#test')[0])





