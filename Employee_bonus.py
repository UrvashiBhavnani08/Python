ch = input("Enter the sex of the employee (m or f): ")
salary = float(input("Enter the salary of the employee : "))
if (ch == 'm'):
    if(salary < 10000):
        newsalary = 0
        newsalary = ((salary*7)/100)
        newsalary += salary
        print("Your Salary : ",salary)
        print("The Salary to be paid: ",newsalary)
    else:
        newsalary = 0
        newsalary = ((salary*5)/100)
        newsalary += salary
        print("Your Salary : ",salary)
        print("The Salary to be paid: ",newsalary)
elif (ch == 'f'):
    if(salary < 10000):
        newsalary = 0
        newsalary = ((salary*12)/100)
        newsalary += salary
        print("Your Salary : ",salary)
        print("The Salary to be paid: ",newsalary)
    else:
        newsalary = 0
        newsalary = ((salary*10)/100)
        newsalary += salary
        print("Your Salary : ",salary)
        print("The Salary to be paid: ",newsalary)

        
