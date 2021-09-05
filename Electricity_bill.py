unit = int(input("Enter the number of units consumed: "))
per = (unit*20)/100
if(unit>=0 and unit<=50):
    unit *= 0.5
    unit += per
    print("Your Pay amount of Electricity bill is: ",unit)
elif(unit>50 and unit<=150):
    unit *= 0.75
    unit += per
    print("Your pay amount of Electricity bill is: ",unit)
elif(unit>150 and unit<=250):
    unit *= 1.20
    unit += per
    print("Your pay amount of Electricity bill is: ",unit)
elif(unit>250):
    unit *= 1.50
    unit += per
    print("Your pay amount of Electricity bill is: ",unit)

