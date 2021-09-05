
year = int(input("Enter the start year number:"))
year1 = int(input("Enter the end year number:"))
year1+=1
for i in range(year,year1):
   if (year % 4) == 0:
      if (year % 100) == 0:
          if (year % 400) == 0:
              print(year)
          
      else:
          print(year1)
   
'''if (year1 % 4) == 0:
      if (year1 % 100) == 0:
          if (year1 % 400) == 0:
              print("{0} is a leap year".format(year1))
          else:
              print("{0} is not a leap year".format(year1))
      else:
          print("{0} is a leap year".format(year1))
   else:
      print("{0} is not a leap year".format(year1))
'''
