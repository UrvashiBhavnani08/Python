fact=1

def factorial(number):
    if(number > 0):
        num=number+1
        for i in range(1,num):
            fact=fact*i
        print("The factorial of the {} is: {}".format(number,fact))
    else:
        print("Please enter a positive number.")
def factorialTrailingZeroes(number):
    pass

if __name__ == '__main__':
    number=int(input("Enter any a number:"))
    fac = factorial(number)
    
