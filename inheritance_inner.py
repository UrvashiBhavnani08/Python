class Parent:
    def __init__(self):
        print("This is a paernt class.")

    class Parent1():
        def m1(self):
            print("This is the Parent inner class.")

class Child(Parent):
    def __init__(self):
        print("This is child class.")
        super().__init__()
        #self.obj=Parent()
        #Parent.Parent1.m1(self)
        super(Parent.Parent1).m1(self)

obj=Child()
