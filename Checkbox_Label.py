import tkinter
from tkinter import messagebox
top = tkinter.Tk()
top.title("This is GUI.")
top.config(cursor="circle")
def print_selection():
    if(var1.get()==1) & (var2.get()==0):
        l.config(text="I love Veg.")
    elif(var1.get()==0) & (var2.get()==1):
        l.config(text="I Love Non Veg")
    elif(var1.get()==0) & (var2.get()==0):
        l.config(text="I don't like anything.")
    else:
        l.config(text="I Love both.")
l = tkinter.Label(top,bg="white",width=20,text=" ")
l.pack()
var1 = tkinter.IntVar()
var2 = tkinter.IntVar()

c1 = tkinter.Checkbutton(top,text="Veg",
                         variable=var1,
                         foreground="red",
                         background="yellow",
                         activebackground="blue",
                         bd=5,
                         font=("Helvetica","16"),
                         command=print_selection)
c1.pack()
c2 = tkinter.Checkbutton(top,
                         text="Non Veg",
                         variable=var2,
                         foreground="red",
                         background="yellow",
                         activebackground="blue",
                         bd=5,
                         font=("Helvetica","16"),
                         command=print_selection)
c2.pack()
top.mainloop()
