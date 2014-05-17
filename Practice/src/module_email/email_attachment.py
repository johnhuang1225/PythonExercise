# coding=utf-8
'''
Created on 2014/5/15

@author: John Huang
'''
import smtplib,os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

msg = MIMEMultipart()
msg['to'] = 'johnhuang@chenbro.com'
msg['from'] = 'johnhuang@chenbro.com'
msg['subject'] = '這是python email-有附件'

att = MIMEText(open('email附件.txt','rb'),'base64','utf-8')
att["Content-Type"] = 'application/octet-stream'
# att["Content-Disposition"] = 'attachment; filename="email附件.txt"'
att.add_header("Content-Disposition", "attachment", filename = os.path.basename('email附件.txt'))
msg.attach(att)

smptserver = smtplib.SMTP('exmail3.chenbro.com.tw', 587)
smptserver.sendmail('johnhuang@chenbro.com', 'johnhuang@chenbro.com', msg.as_string())
smptserver.quit()

print('ok')