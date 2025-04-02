from tkinter import *
yash = Tk()
yash.geometry("700x1000")
yash.title("https://www.amarpunjabiportal.com")
# Creating the Label
a = Label(yash,text="WELCOME TO AMAR PUNJABI\n\nA House of Trust !\n\n",foreground="black",font="Bradley 16 bold",relief=SUNKEN)
a.pack(side=TOP,anchor=N,fill="x")
b = Label(yash,text="Here is the Menu :-",foreground="black",font="InkFree 15 bold")
b.place(x=0,y=100)
c = Label(yash,text=" MatarPaneer - 170rs \n DumAalooGravi - 200rs \n PannerLawabdar - 300rs \n SevTamatar - 160rs \n MixVeg  - 210rs \n TavaSabji - 190rs \n DaalTadka - 180rs \n MalaiKofta - 250rs \n BasmatiRice - 300rs \n Pulaav - 175rs \n TandooriChapati - 20rs \n LacchaParatha - 35rs \n BundiRayta - 200rs \n Custard - 100rs \n GreenSalad - 75rs ",fg="black",font="InkFree 15 bold",borderwidth=6,relief=SUNKEN)
c.place(x=220,y=130)
# Creating a Dictionary
dic = { "matarpaneer" : 170 , "dumaaloogravi" : 200 , "paneerlawabdar" : 300 , "sevtamatar" : 160 , "mixveg" : 210 , "tavasabji" : 190 , "daaltadka" : 180 , "malaikofta" : 250 , "basmatirice" : 300 , "pulaav" : 175 , "tandoorichapati" : 20 , "lacchaparatha" : 35 , "bundirayta" : 200 , "custard" : 100 , "greensalad" : 75 }
# Creating Again label for Entry
l1 = Label(yash,text="Enter the names of Vegis",fg="black",font="InkFree 14 bold")
l1.place(x=0,y=550)
l2 = Label(yash,text="What do you Like to take with Vegis",fg="black",font="InkFree 14 bold")
l2.place(x=0,y=600)
l3 = Label(yash,text="Enter the names of other Things",fg="black",font="InkFree 14 bold")
l3.place(x=0,y=650)
# Define Classes for Entry
c1 = StringVar()
c2 = StringVar()
c3 = StringVar()
# Creating Entry 
e1 = Entry(yash,textvariable=c1,background="white",foreground="black",font="InkFree 14 bold")
e1.place(x=450,y=550)
e2 = Entry(yash,textvariable=c2,background="white",foreground="black",font="InkFree 14 bold")
e2.place(x=450,y=600)
e3 = Entry(yash,textvariable=c3,background="white",foreground="black",font="InkFree 14 bold")
e3.place(x=450,y=650)
# Creating the Button
b1 = Button(yash,text="Order Now",bg="orange",fg="black",font="InkFree 17 bold",borderwidth=6,relief=SUNKEN)
b1.place(x=275,y=700) 
b2 = Button(yash,text="Exit Portal",background="red",foreground="black",relief=SUNKEN,font="InkFree 17 bold",borderwidth=6)
b2.place(x=275,y=750)
b2.bind('<Button-1>',quit)   # "bind" means bhadhna , "quit" is a function which exited and "<Button-1" means Performing task when you click the button in one touch.













yash.mainloop()