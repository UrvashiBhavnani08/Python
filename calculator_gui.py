from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
master = Tk()
master.config(cursor="circle")
master.title("Calculator")
def operation():
    x=e1.get()
    y=e2.get()
    num3=int(x)
    num4=int(y)
    if var1.get() == 1:
        result = num3+num4
        l3.config(text=result)
    elif var1.get() == 2:
        result = num3-num4
        l3.config(text=result)
    elif var1.get() == 3:
        result = num3*num4
        l3.config(text=result)
    elif var1.get() == 4:
        result = num3/num4
        l3.config(text=result)
l1 = Label(master,text="Hey!! You are on Calculator Page.",
           fg="red",
           bg="yellow",
           width=200,
           height=3)
l1.pack()
l2 = Label(master,text="Please enter the two numbers and move ahead.",
           fg="red",
           bg="yellow",
           width=200,
           height=3)
l2.pack()
l3= Label(master,text="Please Choose the operation that you want to perform.",
           fg="red",
           bg="yellow",
           width=200,
           height=3)
l3.pack()
num1 = IntVar()
e1 = Entry(master,textvariable=num1)
e1.pack()
num2 = IntVar()
e2 = Entry(master,textvariable=num2)
e2.pack()
var1 = IntVar()
radiob1 = Radiobutton(master,text="Addition",
                      fg="black",
                      padx=7,
                      pady=7,
                      variable=var1,
                      value=1,
                      command=operation)
radiob1.pack()
radiob2 = Radiobutton(master,text="Subtraction",
                      fg="black",
                      padx=7,
                      pady=7,
                      variable=var1,
                      value=2,
                      command=operation)
radiob2.pack()
radiob3 = Radiobutton(master,text="Multiplication",
                      fg="black",
                      padx=7,
                      pady=7,
                      variable=var1,
                      value=3,
                      command=operation)
radiob3.pack()
radiob4 = Radiobutton(master,text="Division",
                      fg="black",
                      padx=7,
                      pady=7,
                      variable=var1,
                      value=4,
                      command=operation)
radiob4.pack()
l3 = Label(master,bg="white",fg="black",width=30,text=" ")
l3.pack()
master.mainloop()
