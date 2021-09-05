import tkinter
top = tkinter.Tk()
top.config(cursor="circle")
def add():
    result = int(var1.get())+int(var2.get())
    l.config(text=result)
top.title("Hello...")
num1 = tkinter.Label(top,text="Number 1 : ")
num1.place(x=10,y=50)

num2 = tkinter.Label(top,text="Number 2 :")
num2.place(x=10,y=80)

var1=tkinter.StringVar()
var2=tkinter.StringVar()

e1 = tkinter.Entry(top,textvariable=var1)
e1.place(x=80,y=50)
e2 = tkinter.Entry(top,textvariable=var2)
e2.place(x=80,y=80)

b1 = tkinter.Button(top,text="Add",padx=10,pady=10,command=add)
b1.place(x=60,y=120)

l=tkinter.Label(top,text="Result")
l.place(x=60,y=180)

top.mainloop()
