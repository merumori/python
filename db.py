#pip install mysql-connector

import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='')
print(mydb)

#creating database

import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='')
mycursor=mydb.cursor()
mycursor.execute('CREATE DATABASE mpy')


#showing the list of database

import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='')
mycursor=mydb.cursor()
mycursor.execute('SHOW DATABASES')
for i in mycursor:
	print(i)

#creating the 'stud_data' table
#pip install mysql-connector

import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='',database='mpy')
mycursor=mydb.cursor()
mycursor.execute('CREATE TABLE stud_data(roll int,name varchar(25))')

#inserting the record in the table

import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='',database='mpy')
insert_query='INSERT INTO stud_data VALUES (%s,%s)'
record_insert=[(1,'Neel'),(2,'Darshan'),(3,'samir'),(4,'Krunal'),(5,'Harshil'),(6,'Vasu')]
cursor=mydb.cursor()
cursor.executemany(insert_query,record_insert)
mydb.commit()
print("Succesfully")
mydb.close()

#inserting the record in the table

import mysql.connector
try:
	mydb=mysql.connector.connect(host='localhost',user='root',password='',database='mpy')
	insert_query='INSERT INTO stud_data VALUES (%s,%s)'
	record_insert=[(4,'Neel'),(5,'Darshan'),(6,'samir')]
	cursor=mydb.cursor()
	cursor.executemany(insert_query,record_insert)
	mydb.commit()
	print("Succesfully")
except mysql.connector.Error as error:
	print('Failed')	
mydb.close()


#display inserted reeord

import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='',database='mpy')
mycursor=mydb.cursor()
mycursor.execute('SELECT * FROM stud_data')
res=mycursor.fetchall()
# for i in res:
# 	print(i)
print(res)

#update record 

import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='',database='mpy')
mycursor=mydb.cursor()
update_query="UPDATE stud_data SET roll=5 WHERE name='Harshil'"
mycursor.execute(update_query)
mydb.commit()

#delete record

import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='',database='mpy')
mycursor=mydb.cursor()
delete_query="DELETE FROM stud_data"
mycursor.execute(delete_query)
mydb.commit()