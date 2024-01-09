from email.message import EmailMessage
from app2 import password
import ssl
import smtplib

email_sender = 'dushimezar2003@gmail.com'
email_password = password

email_receiver = 'ntakijeredi1@gmail.com'

subject = 'Python Test Mail From Cesar Coder'
body = '''

Hey there!

This is the test mail while sending the email using Python.
It is with an immense pleasure to be able to 
send out this email now finally!

Thank you for helping us out. 

With regards, 
Cesar Coder
'''

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

print("Email was successfully sent to " + email_receiver)
