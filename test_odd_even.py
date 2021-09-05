list1 = []
array = int(input("Please size of array: "))
for i in range(0,array):
    a = int(input())
    list1.append(a)
print(list1)


for j in range(0,len(list1)):
    if j%2 == 0:
        print(list1[j],"even number")
    elif j%2 != 0:
        print(list1[j],"odd number")
    else:
        print("not a valid number.")


#print("3%2",3%2)
