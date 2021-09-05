salary = int(input("Enter the basic pay of your salary: "))
hra = (salary*10)/100
ta = (salary*5)/100
salary += hra + ta
print("The total salary is: ",salary)
