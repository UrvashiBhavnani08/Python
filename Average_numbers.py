a=1
sum1=0
for a in range(1,11):
    b=float(input("Enter the {} number: ".format(a)))
    sum1=sum1+b
print("\n")
average=sum1/10
print("The average of 10 numbers is: ",average)
