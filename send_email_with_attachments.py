import smtplib
from email.message import EmailMessage  #this is needed to create an email subject


email = EmailMessage()
email['From'] = 'your.email@gmail.com'
email['To'] = 'the.receiver@web.de'
email['Subject'] = 'Diesmal mit Betreff'
email.set_content('Hallo\ndies ist nur ein Test.')

#now let's attach the first pdf

with open('C:\\Users\\...\\Emailstuff\\periodictable.pdf', 'rb') as m:
    file_data = m.read()
    file_name = "periodictable.pdf"  #you can choose a name for the receiver to see here

email.add_attachment(file_data, maintype = 'image', subtype = 'octet-stream', filename = file_name)

#now let's attach another pdf

with open('C:\\Users\\...\\Emailstuff\\another_attachment.pdf', 'rb') as m:
    file_data = m.read()
    file_name = "another_attachment.pdf"  #you can choose a name for the receiver to see here

email.add_attachment(file_data, maintype = 'image', subtype = 'octet-stream', filename = file_name)

#and now let's send the email

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login('your.email@gmail.com', 'yourgooglePW')
    smtp.send_message(email)
