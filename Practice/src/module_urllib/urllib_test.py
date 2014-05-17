# coding=utf-8
'''
Created on 2014/5/14

@author: John Huang
'''
import urllib.request

"""
python3    urllib.request
python2    urllib
"""
url = 'http://www.google.com'
with urllib.request.urlopen(url) as url:
    data = url.read()
print(data)