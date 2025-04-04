
from tkinter import *
from datetime import date
# Create Window
root = Tk()
root.title('Getting Started with Widgets')
root.geometry('400x300')
# Add widg
#Add Label
lbl = Label(text="Hey There!", fg="white", bg="#072F5F", height=1, width=300)
# Add Label for getting name as input from user
# Use Entry Widget to create a text box for user to enter details
name_lbl = Label(text="Full Name", bg="#3895D3")
name_entry = Entry()
#Function to display a Message
def display():
#Read input given by user
    name = name_entry.get()
#Declaring a global variable
# to make it accessible anywhere in the program 
    global message
    message= "Welcome to the Application! \nToday's date is: "
    greet = "Hello "+name+"\n"


    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

text_box = Text(height = 3)


btn = Button(text = "Begin", command = display, height = 1, bg = "#1261A0", fg = 'white')


lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()
root.mainloop()