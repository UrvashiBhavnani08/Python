activity = 30.0
sports = 20.0
exam = 50.0
examtotal = 200.0
activities = 60.0
sportstotal = 50.0
escore = int(input("Enter the score obtained in first examination (out of 100) : "))
escore2 = int(input("Enter the score obtained in second examination (out of 100) : "))
sportsscore = int(input("Enter the score obtained in sports activity (out of 50) : "))
activity1 = int(input("Enter the score obtained in the first activity (out of 20) : "))
activity2 = int(input("Enter the score obtained in the second activity (out of 20) : "))
activity3 = int(input("Enter the score obtained in the third activity (out of 20) : "))
activitytotal = 0
activitytotal = activity1 + activity2 + activity3
etoatl = 0
etotal = escore + escore2
activitypercentage = ((((activitytotal * activity)/activities)))
exampercentage = ((((etotal * exam) /examtotal)))
sportspercentage = (((sportsscore * sports) / sportstotal))
total = 0
total = activitypercentage + exampercentage + sportspercentage
print("********************RESULT***********************")
print("Percentage obtained in sports: ",sportspercentage)
print("Percentage obtained in exams : ",exampercentage)
print("Percentage obtained in activities: ",activitypercentage)
print("********************FINAL RESULT***********************")
print("Total percentage : ",total)
