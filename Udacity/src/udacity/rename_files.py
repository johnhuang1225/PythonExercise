# coding=utf-8
'''
Created on 2015/9/8

@author: John Huang
'''
import os

def rename_files():
    work_path = r"D:\Python_workspace\test\prank\prank"
    
    file_list = os.listdir(work_path)
    os.chdir(work_path)
     
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None,"0123456789"))
    
rename_files()
