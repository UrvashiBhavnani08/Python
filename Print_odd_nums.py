list1 = [10,22,35,47,58,65,79,800,91,121]
for i in list1:
    if(i%2 == 0):
        del i
    else:
        print(i,end=" ")
print("\n")
print(list1)
