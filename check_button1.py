
from tkinter import *
from tkinter import messagebox
top = Tk()
top.config(cursor="circle")
def message():
    messagebox.showinfo("Button","My Button pressed")
    
b1 = Button(top,text="Submit",foreground="green",background="red",padx=10,pady=10,command=message)
b1.place(x=600,y=200)
top.mainloop()
