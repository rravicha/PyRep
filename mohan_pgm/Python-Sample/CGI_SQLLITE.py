import sqlite3

conn = sqlite3.connect('test.db')
print ("Opened database successfully")

var = conn.execute('''CREATE TABLE COMPANYy
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         SALARY         REAL);''')
print("Table created successfully")
print(var)
conn.close()

##C:\>set https_proxy = https://sivaraman.m:jan@51713860@campus-proxy:80
##pip install 

#_________________Insert

##import sqlite3
##
##conn = sqlite3.connect('test.db')
##print "Opened database successfully";
##
##conn.execute("INSERT INTO COMPANYy (ID,NAME,AGE,ADDRESS,SALARY) \
##      VALUES (1, 'Paul', 32, 'California', 20000.00 )");
##
##conn.execute("INSERT INTO COMPANYy (ID,NAME,AGE,ADDRESS,SALARY) \
##      VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");
##
##conn.execute("INSERT INTO COMPANYy (ID,NAME,AGE,ADDRESS,SALARY) \
##      VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");
##
##conn.execute("INSERT INTO COMPANYy (ID,NAME,AGE,ADDRESS,SALARY) \
##      VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");
##
##conn.commit()
##print "Records created successfully";
##conn.close()

##################################3

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print ("Database version : %s " % data)

# disconnect from server
db.close()
