from tkinter import *


yash = Tk()

# Page Size
yash.geometry("400x630")


# Page Name
yash.title("https://www.red_bus_travellers.com")
# photo = PhotoImage(file='C:\Users\YASH\Videos\Captures\Canva.png')
# yash.create_image(0,0,anchor=NW,image=photo)

# Creating functions
def f1():
    print("Details is Submitted !")

def f2():
    for x,y in (("Person Name  ",c1.get()),("Mobile No.   ",c2.get()),("From Location",c3.get()),("To Location  ",c4.get()),("Payment Mode ",c5.get()),("PreOrder Meal",a.get())):    # We use the for loop because append not added value more  than one at one Time...
        print(f"{x}  :  {y}")
        
# Welcome Label
l1 = Label(yash,text="Welcome to Red Bus Travellers",font="InkFree 16 bold",bg="white",fg="red")
l1.pack(side=TOP,anchor=N,fill="x")

# Creating Inserting Images


# Creating Labels
l2 = Label(yash,text="Passenger Name ",fg="black",font="InkFree 13 bold")
l2.place(x=0,y=50)

l3 = Label(yash,text="Mobile Number  ",fg="black",font="InkFree 13 bold")
l3.place(x=0,y=100)

l4 = Label(yash,text="From Location  ",fg="black",font="InkFree 13 bold")
l4.place(x=0,y=150)

l5 = Label(yash,text="To Location    ",fg="black",font="InkFree 13 bold")
l5.place(x=0,y=200)

l6 = Label(yash,text=" Payment Mode  ",fg="black",font="InkFree 13 bold")
l6.place(x=0,y=250)

# Define Classes
c1 = StringVar()
c2 = IntVar()
c3 = StringVar()
c4 = StringVar()
c5 = StringVar()

# Creating Entries
e1 = Entry(yash,textvariable=c1,bg="white",borderwidth=5,fg="black",font="InkFree 13 bold")
e1.place(x=200,y=50)

e2 = Entry(yash,textvariable=c2,bg="white",borderwidth=5,fg="black",font="InkFree 13 bold")
e2.place(x=200,y=100)
e3 = Entry(yash,textvariable=c3,bg="white",borderwidth=5,fg="black",font="InkFree 13 bold")
e3.place(x=200,y=150)

e4 = Entry(yash,textvariable=c4,bg="white",borderwidth=5,fg="black",font="InkFree 13 bold")
e4.place(x=200,y=200)

e5 = Entry(yash,textvariable=c5,bg="white",borderwidth=5,fg="black",font="InkFree 13 bold")
e5.place(x=200,y=250)

# Creating Checkbutton
a = IntVar()  # We stored the value of Checkbutton in "a" which is an Integer taking input function So It gives 1 if click the Checkbutton else 0

cb = Checkbutton(yash,relief=SUNKEN,borderwidth=1,text="Wants to pre_order your meal !",font="InkFree 13 bold",variable=a)
cb.place(x=50,y=300)

# Creating Button for submit the Program
b1 = Button(yash,text="Submit Details",font="InkFree 15 bold",bg="grey",fg="white",command=f1,relief=SUNKEN,borderwidth=6)
b1.place(x=125,y=350)

b2 = Button(yash,text="Display Details",font="InkFree 15 bold",bg="red",fg="white",command=f2,relief=SUNKEN,borderwidth=6)
b2.place(x=125,y=400)

# Creating Exit Button
b3 = Button(yash,text="Exit Portal",background="grey",foreground="white",relief=SUNKEN,font="InkFree 15 bold",borderwidth=6)
b3.place(x=140,y=450)
b3.bind('<Button-1>',quit)   # "bind" means bhadhna , "quit" is a function which exited and "<Button-1" means Performing task when you click the button in one touch.


yash.mainloop()  

                                             