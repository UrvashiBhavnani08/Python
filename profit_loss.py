sp = int(input("Enter the selling price of your product: "))
cp = int(input("Enter the cost price of your product: "))
if(sp>cp):
    profit = sp - cp
    print("The profit is: Rs.{} ".format(profit))
elif(cp>sp):
    loss = cp - sp
    print("The loss is: Rs.{} ".format(loss))
elif(sp == cp):
    print("No profit, No Loss.")
