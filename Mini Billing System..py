print("\n\n")
class item:
    def __init__(self,id,name,price):
        self.id = id
        self.name = name
        self.price = price
          

# create bill display function
def Generate_Bill(l,bname,bmobile,baddress):
    print("                                     YASH MART                                                ")
    print("______________________________________________________________________________________")
    print("                                      INVOICE                ")
    print("______________________________________________________________________________________")     
    print(f"Name : {bname}\t            Mob.no: {bmobile} \t               Address : {baddress}")        
    print("______________________________________________________________________________________")
    total = 0
    for a in list:
        print(f"Id  :  {a.id} \t                  Itemname  :  {a.name} \t          Price  :  {a.price}  ")      #  Because we saves it by "self." so we can call id , itemName , price by "a."   .
        print("---------------------------------------------------------------------------------------")
        total = total+a.price
    print("______________________________________________________________________________________")
    print(f" Grand_Total :                                                    {total}") 
    print("  Discount   :                                                    7 % ")  
    c = (total*7)/100 
    print(f" Final_Total :                                                   {total-c}") 
    print("\n")
    
    print("                                   Thankyou Sir !    ") 
    print("\n\n")  
      

# Knowledge is also available when you scroll right the Screen ! So Please Read and Remember .
print("\n")

# Store item array
list = []

print("                                       YASH MART               ")
print("---------------------------------------------------------------------------------------------")
print('\n\n')
bname = input(" Enter name so that we can make the bill of that name -    ")
bmobile = int(input(" Enter your mobile no. -                                   "))
baddress = input(" Enter your Location -                                     ")
totalitem = int(input(" Enter the total quantity of the items -                   "))
print('\n\n')

# Take input items Details 
for i in range(0,totalitem):
    id = i+1
    iname = input(" Enter Name of item -    ")
    iprice = int(input(" Enter the price -  "))
    list.append(item(id,iname,iprice))
print('\n\n')

# Calling the Function
Generate_Bill(list,bname,bmobile,baddress)   
                                 

                                    
                                                             


