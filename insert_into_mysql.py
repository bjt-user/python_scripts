import mysql.connector
from datetime import date

db = mysql.connector.connect(
    host = "localhost",
    user = "mySQLusername",
    passwd = "myPassword",
    database = "myDatabase"
)

mycursor = db.cursor()

#curdate() doesn't seem to work with python, so we need to get the date from python module
today = date.today()

print("Which company did you apply to?")
python_company_name = input()

mycursor.execute("INSERT INTO applications (company_name, application_date) VALUES (%s, %s)", (python_company_name, today))
db.commit()

input()
