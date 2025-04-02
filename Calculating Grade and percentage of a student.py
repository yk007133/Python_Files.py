print("RBSE 12th Board Examination Result :\nPlease fill the followling details : ")

a=input("Enter the Candidate Name:\n")


print("Please entered the following subject's marks:")


b=int(input("English:\n"))
c=int(input("Hindi:\n"))
d=int(input("Physics:\n"))
e=int(input("Chemistry:\n"))
f=int(input("Mathematics:\n"))
g=b+c+d+e+f
print("Total obtained marks out of 500:\n",g)
h=g/500*100
print("Percentage Obtained  :\n",h,"%")
i=g/5
print("Average marks obtained:\n",i)
if i>=91 and i<=100:
    print("Congrats",a,"Your Grade is A1")
elif i>=81 and i<=91:
    print("Congrats",a,"Your Grade is A2")
elif i>=71 and i<=81:
    print("Congrats",a,"Your Grade is B1")
elif i>=61 and i<=71:
    print("Congrats",a,"Your Grade is B2")
elif i>=51 and i<=61:
    print("Congrats",a,"Your Grade is C1")
elif i>=41 and i<=51:
    print("Congrats",a,"Your Grade is C2")
elif i>=33 and i<=41:
    print("Congrats",a,"Your Grade is D1")
elif i>=21 and i<=33:
    print("Congrats",a,"Your Grade is D2")
elif i>=0 and i<=21:
    print("Sorry",a,"you are Fail")
else:
    print("Invalid Input!")


 





