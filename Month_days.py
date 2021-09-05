month=(input("Enter a month name:"))
if (month == "January" or month == "March" or month == "May" or month == "July" or month == "August" or month == "October" or month == "December"):
    print('he number of days of "{}" is : 31'.format(month))
elif(month == "February"):
    print('The number of days of "{}" is : 28'.format(month))
else :
    print('The number of days of "{}" is : 30'.format(month))

