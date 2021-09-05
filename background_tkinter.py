from tkinter import *

gui = Tk(className='Resume using Python tkinter')
# set window size
gui.geometry("595x842")
gui.resizable(0, 0)
back = Frame(master=gui,bg='white')
back.pack_propagate(0)
back.pack(fill=BOTH, expand=1)

#set window color
#gui.configure(bg='white')
gui.configure(cursor="circle")
l1 = Label(gui,
          text="Urvashi Bhavnani",
          bg="white",
          fg="black",
          font=("Helvetica 18 bold underline"),
          cursor="circle",
          padx=2,
          pady=2)
l1.place(x=10,y=10)
l2 = Label(gui,
          text="bhavnaniurvashi@gmail.com \n +91 9427519899 \n Vadodara,Porbandar",
          font=("Helvetica 7"),
          bg="white",
          fg="grey",
          cursor="circle",
          padx=2,
          pady=2)
l2.place(x=450,y=5)
w = Canvas(gui, width=10000, height=100,bg="white")
w.create_line(0, 100, 11300, 100, fill="grey",width=3) 
w.place(x=0,y=45)

l3 = Label(gui,
          text="Education",
          font=("Helvetica 7"),
          bg="white",
          fg="grey",
          cursor="circle",
          padx=2,
          pady=2)
l3.place(x=10,y=160)
l4 = Label(gui,
          text="Bachelor of Computer Applications (BCA)",
          bg="white",
          fg="black",
          font=("Helvetica 10 bold"),
          cursor="circle",
          padx=2,
          pady=2)
l4.place(x=10,y=180)
l5 = Label(gui,
          text="Maharaja Sayajirao Gaikwad College \n 2020 - 2023",
          bg="white",
          fg="grey",
          font=("Helvetica 10"),
          cursor="circle",
          padx=2,
          pady=2)
l5.place(x=10,y=200)
l6 = Label(gui,
          text="Senior Secondary (XII)",
          bg="white",
          fg="black",
          font=("Helvetica 10 bold"),
          cursor="circle",
          padx=2,
          pady=2)
l6.place(x=10,y=240)
l7 = Label(gui,
          text="NIOS board \n Year of completion: 2020",
          bg="white",
          fg="grey",
          font=("Helvetica 10"),
          cursor="circle",
          padx=2,
          pady=2)
l7.place(x=10,y=260)
l8 = Label(gui,
          text="Secondary (X)",
          bg="white",
          fg="black",
          font=("Helvetica 10 bold"),
          cursor="circle",
          padx=2,
          pady=2)
l8.place(x=10,y=300)
l9 = Label(gui,
          text="CBSE board \n Year of completion: 2018",
          bg="white",
          fg="grey",
          font=("Helvetica 10"),
          cursor="circle",
          padx=2,
          pady=2)
l9.place(x=10,y=320)
l0 = Label(gui,
          text="TRAININGS",
          font=("Helvetica 7"),
          bg="white",
          fg="grey",
          cursor="circle",
          padx=2,
          pady=2)
l0.place(x=10,y=360)
label = Label(gui,
          text="Programming For Everybody,Python Basics And Data Science",
          bg="white",
          fg="black",
          font=("Helvetica 10 bold"),
          cursor="circle",
          padx=2,
          pady=2)
label.place(x=10,y=380)
a = Label(gui,
          text="Edx,coursera, \n Online, Duration:- Dec 2020 - Mar 2021",
          bg="white",
          fg="grey",
          font=("Helvetica 10"),
          cursor="circle",
          padx=2,
          pady=2)
a.place(x=10,y=400)
b = Label(gui,
          text="SKILLS",
          font=("Helvetica 7"),
          bg="white",
          fg="grey",
          cursor="circle",
          padx=2,
          pady=2)
b.place(x=10,y=440)
c = Label(gui,
          text="Python \t \t HTML",
          bg="white",
          fg="black",
          font=("Helvetica 10 bold"),
          cursor="circle",
          padx=2,
          pady=2)
c.place(x=10,y=460)
d = Label(gui,
          text="Intermediate \t  Intermediate",
          bg="white",
          fg="grey",
          font=("Helvetica 10"),
          cursor="circle",
          padx=2,
          pady=2)
d.place(x=10,y=480)
g = Label(gui,
          text="CSS \t \t JAVASCRIPT",
          bg="white",
          fg="black",
          font=("Helvetica 10 bold"),
          cursor="circle",
          padx=2,
          pady=2)
g.place(x=10,y=540)
h = Label(gui,
          text="Intermediate \t Intermediate",
          bg="white",
          fg="grey",
          font=("Helvetica 10"),
          cursor="circle",
          padx=2,
          pady=2)
h.place(x=10,y=560)
j = Label(gui,
          text="Projects",
          bg="white",
          fg="black",
          font=("Helvetica 10 bold"),
          cursor="circle",
          padx=2,
          pady=2)
j.place(x=10,y=580)
k = Label(gui,
          text="Desktop Assistant - AI Based \n Resume - Python,tkinter",
          bg="white",
          fg="grey",
          font=("Helvetica 10"),
          cursor="circle",
          padx=2,
          pady=2)
k.place(x=10,y=600)
gui.mainloop()
