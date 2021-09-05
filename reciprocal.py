import array as numbers
numbers=(['a',0,5])
reciprocals=(['a',0,5])
try:
    for val in numbers:

        print("\nThe values of the reciprocals are:\n")
        for i in range(0,numbers,1):
          
            reciprocals[i] = 1.0 / numbers[i]
            print("%15.2lf", reciprocals[i])
          
            print("\n\n")

        for i in range(0, numbers,1):
          
            sum += reciprocals[i]              #Accumulate Sum of reciprocals
            if (i > 0):
              print(" + ")
            print("1/%.2lf", numbers[i])
          
            print(" = %lf\n", sum)
except:
    print("Please try again later.")
