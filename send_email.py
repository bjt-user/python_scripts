#this works (but it only works if the sender has gmail.com as email provider)
#TODO: Attachments hinzufügen

import smtplib
from email.message import EmailMessage  #this is needed to create an email subject

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('firstname.lastname@gmail.com', 'myPassword')

#this is to create a more sophisticated email
email = EmailMessage()
email['From'] = 'firstname.lastname@gmail.com'
email['To'] = 'the.receiver@web.de'
email['Subject'] = 'this is the header'
email.set_content('hello\nthis is just a test.')

server.send_message(email)
