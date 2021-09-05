i=1
num=int(input("Enter the number for multiplication table:"))
m=int(input("Enter until the number you want:"))
m+=1
for i in range(1,m):
    print("{0} * {1} = {2}".format(num,i,num*i))
print("\n")
