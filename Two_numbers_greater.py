num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if(num1 > num2):
    print("{} is greater than {}.".format(num1, num2))
elif(num2 > num1):
    print("{} is greater than {}.".format(num2, num1))
elif(num1 == num2):
    print("{} and {} are equal.".format(num1, num2))
else:
    print("Please enter a valid number.")
