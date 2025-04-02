from tkinter import *
from tkinter.ttk import *
from time import strftime 

yash = Tk()

yash.title("Digital Clock")


def time():
    dhruv = strftime("%H:%M:%S %p")  #"strftime" converts string based specific format of date & time 
    label.config(text=dhruv)
    label.after(1000, time)  

label = Label(yash,font=("ds-digital" , 80),background="black",foreground="lightgreen")
label.pack(anchor='center')
time() 
yash.mainloop()       


                                                         

                                                  