a=1
b=1
cs=5
cs+=1
for a in range(1,cs):
    a+=1
    for b in range(1,a):
        print("{}".format(b),end=" ")
    print("\n")
