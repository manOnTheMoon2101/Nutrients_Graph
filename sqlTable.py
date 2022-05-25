import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="my_diet"
  
)

'''
CREATING DATABASE
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE my_diet)

'''

'''
CREATING TABLE
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE calories(day INT AUTO_INCREMENT PRIMARY KEY,food int,burned int,deficit int))

'''

'''
Inserting DATA
mycursor = mydb.cursor()

mycursor.execute("INSERT INTO calories(food,burned,deficit) values(607,702,-95),(694,751,-57))

'''

mycursor = mydb.cursor()

mycursor.execute("Select * from calories")

