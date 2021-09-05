from tkinter import *
master = Tk()
var1 = IntVar()
Checkbutton(master,text='male',variable=var1).pack()
var2 =IntVar()
Checkbutton(master,text="female",variable=var2).pack()
mainloop()
