import sqlite3
cnt = sqlite3.connect('au.dp')

cnt.execute('create table stud_data(roll integer, name varchar)')
print('Table Created')

cnt.execute('insert into stud_data values(1, "Amit")')
cnt.execute('insert into stud_data values(2, "Amit")')
cnt.execute('insert into stud_data values(3, "Amit")')
print('Record Inserted Successfully')
cnt.commit()

cursor = cnt.execute('select * from stud_data')
for i in cursor:
    print(i)

cursor = cnt.execute('select * from stud_data where roll > 2')
for i in cursor:
    print(i)

sql_upd = """Update stud_data set name='April' where roll=3"""
cnt.execute(sql_upd)
cursor = cnt.execute('select * from stud_data')
for i in cursor:
    print(i)

sql_del = """delete from stud_data where roll=3"""
cnt.execute(sql_del)
cursor = cnt.execute('select * from stud_data')
for i in cursor:
    print(i)