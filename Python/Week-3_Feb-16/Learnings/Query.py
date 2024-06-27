import mysql.connector   
mydb = mysql.connector.connect(    
  host="localhost",       
  user="abc",
  password="password"     
)
#This cursor will enable all data stored in mydb to execute(We need a mouse pointer to execute queries)
mycursor = mydb.cursor()  
# mycursor.execute("select * from test1.test_table1")
mycursor.execute("select C1,C2 from test1.test_table1")
#This query will give output in iterable mode so use a for loop
for i in mycursor.fetchall():
    print(i)
mydb.close()   #Close connection every time 