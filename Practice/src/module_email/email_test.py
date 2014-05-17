# coding=utf-8
'''
Created on 2014/5/15

@author: John Huang
'''
import smtplib
from email.mime.text import MIMEText

"""不驗證發送email"""
def sendmail_no_verify(addr_from, addr_to, smtp_server):
    
    msg = MIMEText('這是python email', _charset='utf-8')
    msg['From'] = addr_from
    msg['To'] = addr_to
    msg['Subject'] = '這是python email'
    smptserver = smtplib.SMTP(smtp_server, 587)
    smptserver.set_debuglevel(True)
    smptserver.sendmail(addr_from, addr_to, msg.as_string())
    smptserver.quit()
    print('sendmail_no_verify() ok')
    

    
sendmail_no_verify('johnhuang@chenbro.com', 'johnhuang@chenbro.com', smtp_server='exmail3.chenbro.com.tw')




    
