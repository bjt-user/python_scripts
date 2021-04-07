import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "mysqlusername",
    passwd = "mysqlpassword",
    database = "mydatabase"
)

mycursor = db.cursor()

mycursor.execute("SELECT * FROM applications")

for x in mycursor:
    print(x)
    
print("\n\nPress any key to exit.")
input()
