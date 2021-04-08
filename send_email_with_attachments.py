#TODO: attach multiple pdfs

import smtplib
from email.message import EmailMessage  #this is needed to create an email subject


email = EmailMessage()
email['From'] = 'your.email@gmail.com'
email['To'] = 'the.receiver@web.de'
email['Subject'] = 'Diesmal mit Betreff'
email.set_content('Hallo\ndies ist nur ein Test.')

with open('C:\\Users\\...\\Emailstuff\\periodictable.pdf', 'rb') as m:
    file_data = m.read()
    file_name = "periodictable.pdf"  #you can choose a name for the receiver to see here

email.add_attachment(file_data, maintype = 'image', subtype = 'octet-stream', filename = file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login('your.email@gmail.com', 'yourgooglePW')
    smtp.send_message(email)
