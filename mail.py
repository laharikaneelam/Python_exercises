import smtplib
from email.mime.text import *
body='''hi re this is laharika i am sending this mail from my python program'''
msg=MIMEText(body)
msg['from']="luckyneelam97@gmail.com"
msg['to']="143sarvani@gmail.com"
msg['subject']="hi sarru"
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("luckyneelam97@gmail.com","143momanddad")
server.send_message(msg)
print("message sent....")
server.quit()