sub1 = float(input("Enter the marks obtained in subject 1: "))
sub2 = float(input("Enter the marks obtained in subject 2: "))
sub3 = float(input("Enter the marks obtained in subject 3: "))
sub4 = float(input("Enter the marks obtained in subject 4: "))
total = sub1 + sub2 + sub3 + sub4
avg = (total/4)
if (avg>75):
    print("Distinction")
elif (avg >= 60 and avg <75):
    print("First Division")
elif (avg >= 50 and avg < 60):
    print("Second Division")
elif (avg >= 40 and avg < 50):
    print("Third Division")
else :
    print("Fail")
