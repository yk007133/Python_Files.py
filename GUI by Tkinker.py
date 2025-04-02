# All the Comments of  Information Available in this code read carefully for understanding the GUI Applying  .
# If you wants to learn gui basis then go to red bus project after reading all syntex under bellow ...
from tkinter import *
yash_root = Tk()     # It is a Base of gui and it is necessary to make.

#All code is written b/w Tk() and mainloop() .
yash_root.geometry("900x650")         #given size and easily changable
# WIDTHxHEIGHT
yash_root.minsize(200,100)       # it is its  min size
yash_root.maxsize(1000,700)      # it is its  max size
# WIDTH, HEIGHT 

yash_root.title("My GUI With Yash")   # this is a name generator of our GUI File 

# Wants to Text and Adding Image then you can Do it by the Label Method .

   # 1. Label method for text anything



#  Attributes/Features  For Label method for text anything
# bg = backgroundcolor
# fg = font colour 
# padx - x padding
# pady - y padding
# relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE

# when we created label,frames...method  then classname dena must he ex. jese mene "Label" ke ander diya he "yash_root" iska matlab ye he ki aap labelling kis ke ander karna chahate ho .
# iska matlab ye nhi he ki hamesha  classname hi likha jayega dekho ase he ki hume labelling,framing jiske ander karni he uska name aayega ok,jese yaha par hume class ke ander karna tha.  

yas = Label(yash_root,text ='''           
Abdul Rashid Salim Salman Khan is an Indian  
\nfilm actor, producer, occasional playback singer and television personality. In a film career spanning 
\nalmost thirty years, Khan has received numerous awards, including two National Film Awards as a film 
\nproducer, and two Filmfare Awards for acting. He has a significant following in Asia and the Indian 
\ndiaspora worldwide, and is cited in the media as one of the most commercially successful actors of Indian 
\ncinema. According to the Forbes 2018 list of Top-Paid 100 Celebrity Entertainers in world, Khan was 
\nthe highest ranked Indian with 82nd rank with earnings of $37.7 million.''', bg ="yellow", fg="black", padx=20, pady=20, font="InkFree 13 bold", borderwidth=10, relief=GROOVE)

# after Labeling , pack/grid  is must at same name of labeling for showing label in gui page else nothing.

# Attributes/Featurtes for pack...
# anchor = position like nw, ew, sw, ne, se...
# side = top, bottom, left, right
# fill = geometry x,y mein kechne par label bhi x ya y mein expand hoo.
# padx=x mein phelana
# pady=y mein phelana

yas.pack(side=LEFT, fill=Y, padx=34, pady=34)

#  2. Label method for apply images ...

# Use of "PhotoImage"  method the Label Method to execute photo ...

#abc = PhotoImage(file="")

# as same as that we use label method ...

#label = Label(image=abc)

# then pack it as same ...

#label.pack()  
# if wants to make frame and button then see below .
# and one more thing , attributes of pack and label are also use in these button and frames also.

f1 = Frame(yas,bg='black',borderwidth=8,relief=SUNKEN)
f1.pack(side=LEFT)

# Frame is not seen until we not labelling the Frame ok .


dhru = Label(f1,text="This is a Frame",bg="black",fg="white")
dhru.pack()


yash_root.mainloop()  # It is main logic of gui and also it is necessary to make.
   
# To make expert in GUI then watch my all files of GUI...
                                                                                        