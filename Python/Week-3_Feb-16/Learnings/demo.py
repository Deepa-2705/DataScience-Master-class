import mysql.connector   #Import this connector
mydb = mysql.connector.connect( #Anything we will create(table) it will get stored in the mydb variable   
  host="localhost",       # connection happens with the local or same machine
  user="abc",
  password="password"     #Syntax for connection
)
print(mydb)     #Print variable so that if any error comes it will print it
mycursor = mydb.cursor()  #This cursor will enable all data stored in mydb to execute(We need a mouse pointer to execute queries)
mycursor.execute("SHOW DATABASES")    #Show all the databases inside mysql
for x in mycursor:  
  print(x)