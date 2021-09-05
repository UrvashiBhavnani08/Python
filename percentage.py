phy=float(input("Enter the marks of physics out of 100:"))
chem=float(input("Enter the marks of chemistry out of 100:"))
bio=float(input("Enter the marks of biology out of 100:"))
math=float(input("Enter the marks of mathemetics out of 100:"))
comp=float(input("Enter the marks of computer out of 100:"))
total=phy+chem+bio+math+comp
percentage=(total/500)*100
print("Total Marks = %.2f" %total)
print("Marks percentage = %.2f" %percentage)
if(percentage>=90):
    print("You have scored Grade A.")
elif(percentage>=80):
    print("You have scored Grade B.")
elif(percentage>=70):
    print("You have scored Grade C.")
elif(percentage>=60):
    print("You have scored Grade D.")
elif(percentage>=40):
    print("You have scored Grade E.")
else:
    print("You have scored Grade F.")

