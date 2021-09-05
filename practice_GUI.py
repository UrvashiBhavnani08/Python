from tkinter import *
from tkinter import messagebox
window = Tk()
window.config(cursor="circle")
window.title("Urvashi")
b1 = Button(window,text="Submit",activebackground="red",activeforeground="yellow",padx=3,pady=4,underline=2)
b1.pack()
var1 = IntVar()
e1 = Entry(window,text="Name",bd=5,textvariable=var1)
e1.pack()
window.mainloop()
