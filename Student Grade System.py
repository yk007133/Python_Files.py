print('\n')
a={ }

def Execute_function():
    print("                  Student Grade System ")
    print('\n')
    print(" You can choice any one of following option- ")
    print('\n')
    print(" NOTE :- Firstly you will add a student to get more  feature  of this program otherwiswe Function will not response!")
    print('\n')
def add_name(name,grade):
    if name in a:
        print(" The",name,"is already having in my List\n","Please enter an another name!")
    else:
        a[name]=grade
        print( name,'is successfully Added!')

def update(name,grade):
    if name in a:
        a[name]=grade  #  IN THIS CONDITION DUE TO SAME NAME AND DIFF. VALUE SO IT UPDATE THE VALUE OF KEY
        print( name,'is successfully Updated!')
    else:
        print(name,"is not present in our List")

def delete(name):
    if name in a:
        del a[name]
        print( name,'is successfully Deleted!')
    else:
        print(name,"is not present in our List")
         
def displaynames():
    for name,grade in a.items():
        print(f" {name} : {grade}")

Execute_function()
print(" 1. Add a Student")
print(" 2. Update")
print(" 3. Delete")
print(" 4. Display Names")
print(" 5. Exit from the Program") 
print('\n')
while True:
    print("\n")
    choice=input(" Please enter a choice from following options(1-5) - ")
    print('\n') 
    if choice == '1':
        name=input(" Enter the student name - ")
        grade=int(input(" Enter the Grade of student - "))
        print('\n')
        add_name(name,grade)
        print("\n")
    elif choice == '2':
        name=input(" Enter the student name - ")
        grade=int(input(" Enter the Grade of student - "))
        print('\n')
        update(name,grade)
        print("\n")
    elif choice == '3':
        name=input(" Enter the student name - ")
        print("\n")
        delete(name) 
        print("\n")
    elif choice == '4':
        displaynames()
        print("\n")
    elif choice == '5':
        print(" Thankyou Sir ! ")
        print("\n")
        print("\n")
        break
    else:
        print("\n")
        print(' Please choose a valid option! ')










