# 1. Create Connection
import mysql.connector as yash   # We use yash as a alyase so that we use yash in place of mysql.connector   .
a=yash.connect(host="localhost",user="root",password="W7301@jqir#") # Ex = time.sleep(x)

print(a,"Connection Established")

# Ater run if nothing print beside the string then means connection between python and mysql is Established...

# 2. Create Database
# use of cursor method in that variable by which python-mysqlconnnector connection is made, for performing the mysql query in python language .
b=a.cursor()   # Now we perform mysql query in python language and All Things are stored in it .
b.execute("create database DipendraGoyal")    #  execute is a method of b .
print("Database is Created !")  # And You don't make database of same letter name rather then it is capital or small letter .

# NOTE :- Execute is the method of b and it is used to execute something like Database,Table,Insert,Update,Delete,Truncate,etc .

# Wants to see databases then go into the command prompt the type "mysql -u root -p" and enter password after it type "show databases;" ,Then you see the names of all databases are present...

# 3. Create table , database name is compulsory .
a = yash.connect(host="localhost",user="root",password="W7301@jqir#",database="DipendraGoyal")
b = a.cursor()
b.execute("create table Pranjal(Roll int,Ename varchar(20))")  # Table is Created in b and execute is also a method of b  .
print("Table is Created !")
# Where Roll and Ename are the name sof column present in the table .
# Where int means in Roll column integer value done and varchar means in Ename string value is done .


# 4. Show Tables
# use of for-loop wants to display the Tables .
b.execute("show tables")       # By this Command we only See  the names of Table .
for i in b:    # Because of we created the table in b .
    print(i) 

# 5. Insert Record in Table .  
# Process of Connection between mysql and python and Process of making perform mysql query in python language are Compulsory for all Steps . 
b.execute("insert into Emp(Roll,Ename) values(%s,%s)",(10,"Sarthak"))  # For One Data Inserted !
a.commit()   # So commit is a method of a , it is necessary for insert the Data .
print("Recorded is Inserted !")
# wants to See the Inserted Record in Cmd then type "select * from DipendraGoyal.Emp;"




# NOTE :-  When you run the program then you will see an error due to the all of this written one by one and you know that in mysql same Character name rather than capital or samll letter is not Created morer than once So if you apply an individual step in diff. pages then program is successfully Executed .
# NOTE :-  The use of execute method is to perform the sql queries .



# Wants to Inserted Multiple Value at One time use this Way :-
g = "insert into Emp(Roll,Ename) values(%s,%s)"
list = [(30,"Anish"),(40,"Altaf"),(50,"Rohit")]
b.executemany(g,list)
a.commit()

# 6. Select Record Display In The Python Terminal !
b.execute("select * from DipendraGoyal.Emp")
m = b.fetchall()    # fetchall is also a method of b .
print(m)     # In Which all Record is print in a List .
 
# Wants to see in One by One Form then Use of for-loop:-
b.execute("select * from DipendraGoyal.Emp")
m = b.fetchall()
for z in m:
    print(z)


# 7. Update Records 
o = "update DipendraGoyal.Emp set roll=%s where Ename=%s"
s = (60,"Rohit")
b.execute(o,s)
a.commit()
print("Record is Updated !")

# 8.  One Delete Record 
v = "delete from DipendraGoyal.Emp where Ename=%s"
y = ("Rohit",)  # Comma is Compulsory in that step of Delete .
b.execute(v,y)
a.commit()
print("Record  is Deleted !")

# 9. All Record Delete
z = "truncate table DipendraGoyal.Emp"
b.execute(z)
a.commit()
print("All Record Deleted !")
a.close()
b.close()





#************************************** THANKYOU GUYS ! **********************************************************************











