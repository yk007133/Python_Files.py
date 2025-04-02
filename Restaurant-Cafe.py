print("\n")
print("***********  HUNNY-BUNNY   CAFE  AND  RESTAURENT  **********")
print("\n")
print(" Hello !  Sir/Madam\n","Welcome to our Cafe\n","The menu card is here :-")
print("\n")
items = { "Pizza" : 120 , "Paties" : 40 , "Burger" : 50 , "Ice Cream" : 75 , "Maggie" : 60 , "Noddles" : 55 ,"Hotdog" : 65 , "Momos" : 45 , "Sandwich" : 80 , "Pasta" : 90 }
print("                  Pizza         -         120₹\n","                 Paties        -         40₹\n","                 Burger        -         50₹\n","                 Ice Cream     -         75₹\n","                 Maggie        -         60₹\n","                 Noddles       -         55₹","                                   Hotdog        -         65₹","                                   Momos         -         45₹","                                   Sandwich      -         80₹","                                   Pasta         -         90₹")
print("\n")
a=input(" Enter the name of item which wants to order:\n")
print("\n")
total=0
i=0
while i==0:
	if a.title() in items:
		total=total+items[a.title()]
		b=input(" Please enter (yes/no) if you want to order another item or  not:- ")
		print("\n")
		c=0
		while c==0:
			if b.lower()=="yes":
				d=input(" Enter name of item :\n ")
				e=0
				while e==0:
					if d.title() in items:
						print("\n")
						total=total+items[d.title()]
						print(" The total value of your order is - ",total,"₹")
						break
					else:
						print(" Entered value is not present in our cafe")
						d=input(" Enter name of item :\n ")
				break
			elif b.lower()=="no":
				print(" The total value of your order is -",total,"₹")
				break
			else:
				print(" Please entered a valid option")
				b=input(" Please enter (yes/no) if you want to order another item or  not:- ")
		break
	else:
		print(" Entered item is not present in our cafe")
		a=input(" Enter the name of item which wants to order:\n")
print("\n\n"," Choose option under below for payment:-\n")
print("\n")
print(" 1. Net Banking\n", "2. UPI \n","3. Crerit Card\n","4. Cash on Delivery")
print("\n")
g= input()
h=0
while h==0:
		if g.lower() == "net banking":
			l=input(" Enter your password- ")
			print(" Thankyou")
			print("\n")
			print(" Our delivery boy will deliver your order soon!")
			break
		elif g.lower()=="upi":
			l=input(" Enter your password- ")
			print(" Thankyou")
			print("\n")
			print(" Our delivery boy will deliver your order soon!")
			break
		elif g.lower()=="credit card":
			l=input(" Enter your password- ")
			print(" Thankyou")
			print("\n")
			print(" Our delivery boy will deliver your order soon!")
			break
		elif g.lower()=="cash on delivery":
			print("\n")
			
			print(" Thankyou")
			print("\n")
			print(" Our delivery boy will deliver your order soon!")
			break
		else:
			print(" Please select a valid option")
			print("\n")
			g= input()
			
			
			
		
	
		
		
		
		
		
		
		
		
	
			
				
				
				

	    	
	    
	  
	    	
	   	
	    
