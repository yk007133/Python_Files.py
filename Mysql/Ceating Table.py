import mysql.connector as yash 
a = yash.connect(host="localhost",user ="root",password="W7301@jqir#",database="Party")
print("Connection is Established !")
b = a.cursor()  

# NOTE :- Try to put Database name at a time of connnection so that chances of error is minimized .
# NOTE :- We already create Database named "Party" so don't Worry .
# NOTE :- If you run this program then it will show you an error because of I already run this program at a time of Creating .

print("\n") 
print("Now You Perform any Mysql Query !")
print('\n')
b.execute("create table list(Item varchar(10),Price int)")
print("Table is Succesfully Created !")
print("\n")
c = "insert into list(Item,Price) values(%s,%s)"
d = [("Burger",200),("Pizza",120),("Coldrink",90),("Desert",150),("Meal",380)]
b.executemany(c,d)
a.commit()
print("Record is Inserted Successfully !")
print("\n")
b.execute("select * from party.list")    # For showing in Python Terminal .
e = b.fetchall()
for i  in e:
    print(i)
print("\n","Thankyou Dud !")   
a.close()
b.close()     

