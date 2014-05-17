# coding=utf-8
'''
Created on 2014/5/15

@author: John Huang

example from
1)http://stackoverflow.com/questions/3362600/how-to-send-email-attachments-with-python
2)http://code.activestate.com/recipes/578150-sending-non-ascii-emails-from-python-3/

'''
import smtplib, os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import COMMASPACE, formatdate
from email import encoders
from email.header import Header


def send_mail(send_from, send_to, subject, text, files=[], server="localhost"):
    assert isinstance(send_to, list)
    assert isinstance(files, list)

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text,_charset='utf-8'))

#     for f in files:
#         part = MIMEBase('application', "octet-stream")
#         part.set_payload( open(f,"rb").read() )
#         encoders.encode_base64(part)
#         part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
#         msg.attach(part)
    
    for f in files:
        fname = os.path.basename(f)
        
        with open(f, 'rb') as file:
            part = MIMEBase('application', "octet-stream")
            part.set_payload(file.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment', filename=(Header(fname, 'utf-8').encode()))            
            msg.attach(part)
    
    smtp = smtplib.SMTP(server, 587)
#     ad_account='*****'
#     ad_password='*****'
#     smtp.login(ad_account,ad_password)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()


    
send_from = 'johnhuang@chenbro.com'
send_to = ['johnhuang@chenbro.com']
subject = 'Python email attachment'
text = ' Dear All:\n\n附上 Python 電子書  PDF 檔 \n謝謝! '
files = ['D:\John\WORK\eBooks\Python\The Quick Python Book, Second Edition (2010).pdf']
server = 'exmail3.chenbro.com.tw'
send_mail(send_from, send_to, subject, text, files, server)

print('ok')
