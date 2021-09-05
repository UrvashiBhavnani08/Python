a=1
b=1
cs=int(input("Enter the number of rows of you want:"))
a=cs
for a in range(a,0,-1):
    a+=1
    for b in range(1,cs):
        print("{} ".format(b),end=" ")
    print("\n")

