import sqlite3
connection=sqlite3.connect('data.db')

cursor=connection.cursor() #used to run a query and access the result

#1)Createing the table
create_table="CREATE TABLE users (id int,username text,password text)"
cursor.execute(create_table)

#2)Store the data in database

user=(1,'jose','jose123')

insert_user="INSERT INTO users VALUES (?,?,?)"
cursor.execute(insert_user,user)

#Inserting batch of users
users=[
(2,'jay','jay123'),
(3,'saurabh','saurabh123')
]

cursor.executemany(insert_user,users)

#Retriving the data

select_query="SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)

#3)Save the changes
connection.commit()

#4)Close the connection
connection.close()
