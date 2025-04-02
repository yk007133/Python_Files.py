print("*****************  KAUN  BANEGA  CROREPATI *****************")
print('\n')
print("                      Welcome to KBC         ")
print('\n')
questions =[" 1.  Current Railway minister of India?"," 2.  Current President of India?"," 3.  When was Kalinga War started?"," 4.  Founder of Chola dynasty?"," 5.  Guru of lord Krishna?"," 6.  Founder of game chess?"," 7.  Which palace where lord krishna born?"]
options =[ [' A. Ashwini Vaishnaw', ' B. Rajat kumar', ' C. Vivek Bhatnagar', ' D. Dinesh Dixit'],[' A. Pranav Mukharjee', ' B. Draupadi Murmu',' C. Pratibha Patil',' D. Sarojni Naido'],[' A. 340BC',' B. 450BC',' C. 103BC',' D. 261BC'],[' A. Vijayala Chola',' B. Harshvardhan Chola',' C. Vikramaditya Chola',' D. Aditya Chola'],[' A. Gargacharya',' B. Vasudeva',' C. Vishwamitra',' D. Kulgurukrip'],[' A. Gune Ci',' B. Cye Lu',' C. Kim Jeen',' D. Han Xin'],[' A. Vrindavan',' B. Mathura', ' C.  Gokul',' D. Dwarika'] ]
answers =["A","B","D","A","A","D","B"]
levels =['1000₹','5000₹','10000₹','50000₹','100000₹','5000000₹','10000000₹']
earn =['0₹','1000₹','5000₹','10000₹','50000₹','100000₹','5000000₹']

y=0
c=0     #so that the computer cleared the initial value of given things

d=0

for i in questions:
		print(levels[d].center(105))
		d=d+1
		print(i)
		print('\n')
		
		for a in options[y]:
			print(a)
		y=y+1
		    
			
		b=  input(" Enter option which you want\n" )
		if b.upper() ==answers[c] and y<=6:
			print(' Correct')
			c=c+1
		elif  y==7 :
			print(' Correct\n',' CONGRATULATIONS , YOU WIN',levels[6])
			print(" Thankyou")
		
		else:
			print(' Wrong Ans.')
			print(" You only earn",earn[d-1])
			print(" Thankyou")
			break
print('\n')	
print(" Please enter your account no. and IFSC code \n")
n=input()
q=input()
print("\n")
print(" Your winning ammount will credited to your account as early as possible!")
print(" Have a nice Day")	
			
			
		
	    
		
		
		
			
		

		   
		
		
		
		
		

		          
		
		
		