import mysql.connector   
mydb = mysql.connector.connect(    
  host="localhost",       
  user="abc",
  password="password"     
)
#This cursor will enable all data stored in mydb to execute(We need a mouse pointer to execute queries)
mycursor = mydb.cursor()  
#We can insert the same data multiple time in the database as well
mycursor.execute("Insert into test1.test_table1 values(48674,'Deepa',87634,455.635,'Gupta')")
mycursor.execute("Insert into test1.test_table1 values(48674,'Deepa',87634,455.635,'Gupta')")
mycursor.execute("Insert into test1.test_table1 values(48674,'Deepa',87634,455.635,'Gupta')")
mycursor.execute("Insert into test1.test_table1 values(48674,'Deepa',87634,455.635,'Gupta')")
mycursor.execute("Insert into test1.test_table1 values(48674,'Deepa',87634,455.635,'Gupta')")
mydb.commit()  #It will make the changes permanently
mydb.close()   #Close connection every time