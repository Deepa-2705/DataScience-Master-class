#We will study databases using python in this lecture
#Whenever we create an application we have to store data and we store data in some databases 
#We have seen we are storing data in datatype that availabel till runtime and we are storing data in a separate file as well.
#But all this is not effective on large scale 

#We can divide broadly the databases into 2 parts: SQL(Structured Query Language) and NOSQl(Not only sequeal)
# SQL(Only structured data)              NOSQL(unstructured data like audio file,text file)
# 1.Mysql                               Mongodb
# 2.Mssql                               cassandra
# 3.DB2                                 Hbase
# 4.Oracle                              influx
#                                       new4j
  
#This entire sequeal server is hosted on aws or on the same server we are hosting the python.So both are available in same lab
#Create connection and then databases and the tables
#we notice once we create the database then we cant create other database of the same name (this is structured query language)

#Our task is to run sql query in python for that first we have to build connection between python and sequeal 




import mysql.connector   #Import this connector
mydb = mysql.connector.connect( #Anything we will create(table) it will get stored in the mydb variable   
  host="localhost",       # connection happens with the local or same machine
  user="abc",
  password="password"     #Syntax for connection
)
print(mydb)     #Print variable so that if any error comes it will print it
mycursor = mydb.cursor()  #This cursor will enable all data stored in mydb to execute(We need a mouse pointer to execute queries)
mycursor.execute("CREATE DATABASE if not exists test1")     #Write keywords in capital letters
mycursor.execute("CREATE TABLE if not exists test1.test_table1(C1 INT ,C2 VARCHAR(40),C3 INT,C4 FLOAT,C5 VARCHAR(40))")
mydb.close()   #Close connection every time


#In the terminal code 0 means it executed successfully
#In the terminal code 1 means it not executed successfully