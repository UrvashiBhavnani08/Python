a=1
b=1
cs=int(input("Enter the number of rows you want:"))
cs+=1
for a in range(1,cs):
    a+=1
    for b in range(1,cs):
        print("{}".format(b),end=" ")
    print("\n")
