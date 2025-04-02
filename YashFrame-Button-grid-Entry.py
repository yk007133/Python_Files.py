from tkinter import *
yash = Tk()
#yash.geometry("150x175")
#yash.title("Yash")

#f1 = Frame(yash,bg='black',borderwidth=10,relief=SUNKEN)
#f1.pack(side=LEFT,anchor=NW)


#l1 = Label(f1,text="This is a Frame",bg="grey",fg="black",font="InkFree 13 bold")
#l1.pack()

#def prin():
#    print("HI yash How are YOU !")
    

#b1 = Button(f1,text="     Button     ",bg="orange",fg="black",font="InkFree 13 bold",command=prin,borderwidth=5,relief=SUNKEN)
#b1.pack()


#def prin1():
#    print(" How can i help you !")


#b2 = Button(f1,text="     Button     ",bg="white",fg="black",font="InkFree 13 bold",command=prin1,borderwidth=5,relief=SUNKEN)
#b2.pack()


#def prin2():
#    print("Ok Thanks Yash Good Bye !")


#b3 = Button(f1,text="     Button     ",bg="green",fg="black",font="InkFree 13 bold",command=prin2,borderwidth=5,relief=SUNKEN)
#b3.pack()



#yash.mainloop()       
yash.geometry("220x175")                   
yash.title("Dancing Candidates Submission")
l1 = Label(yash,text="Dancing Candidates Submission",bg="grey",fg="black",relief=SUNKEN,borderwidth=8)
l1.pack(side=TOP,fill="x")


f1 = Frame(yash,bg='black',borderwidth=6,relief=SUNKEN)
f1.pack(side=LEFT,anchor=NW)

l2 = Label(f1,text="Enter Name",bg='cyan',fg='black') 
l2.pack()

d=[ ]

def submit():
    d.append(a.get())
    



def display():
    print(d)
    
   










a=StringVar()       # Use " print(a.get()) " to print this type of varaiable in gui....

b=Entry(yash,textvariable=a,borderwidth=9,relief=SUNKEN)
b.pack(side=LEFT,anchor=N,fill="x")

# Use of "place" instead of pack,grid if wants to fit the position of the buttons and frames and you do not need to pack further it ...

#And in grid we use row and coloum as a arguments whereas in place we use x,y as a arguments...

b1=Button(yash,bg='yellow',text='                 Submit              ',fg='black',borderwidth=12,relief=SUNKEN,command=submit)
b1.place(x=20,y=70)

b2 = Button(yash,bg='violet',text="         Display Names        ",fg="black",borderwidth=12,relief=SUNKEN,command=display)
b2.place(x=20,y=120)

































yash.mainloop()
