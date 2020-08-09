'''
Pre-requisites:  
1. Turn of Avast antivirus e-Mail agent.
2. Allow access to less secure apps on G-mail.
3. Prefer port 587 over port 25 for transmission - 25--> server to server(msg relaying) and 587 --> client to server.
4. Use TLS protocol for user-auth(gmail) - line-18  
'''


import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmail.com',587)  ##Server for specific mail service, and protocol for smtp=587/25
server.ehlo() #start the process
server.starttls() 

with open('my_password.txt','r') as f:
    pwd = f.read()
server.login('sender@gmail.com',pwd)


msg = MIMEMultipart()
msg['From'] = 'Dharani'
msg['To'] = 'receiver@gmail.com'
msg['Subject'] = 'Testing my mailing client'

with open('message.txt','r') as f:
    message = f.read()

msg.attach(MIMEText(message,'plain')) #Attaching plain text to the body

#adding actual attachments
filename = 'images.jpg'
attachment = open(filename,'rb')

p = MIMEBase('application','octet-stream')

p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition',f'attachment; filename=(filename)')
msg.attach(p)

text = msg.as_string()
server.sendmail('sender@gmail.com','receiver@gmail.com',text)

print("Email sent successfully! :)")