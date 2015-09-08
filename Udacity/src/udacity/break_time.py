# coding=utf-8
'''
Created on 2015/9/8

@author: John Huang
'''
import time
import webbrowser

i = 0
print("This program started on " + time.ctime())
while i < 3:
    time.sleep(3)
    webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
    i = i + 1