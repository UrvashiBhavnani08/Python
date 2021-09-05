import array as numbers
numbers=(['a',0,5])
reciprocals=(['a',0,5])
try:
    for val in numbers:

        print("\nThe values of the reciprocals are:\n")
        try:
            
            
            for i in range(10):
              
                reciprocals[i] = 1.0 / numbers[i]
                print("%15.2lf", reciprocals[i])
        except BaseException:
            print("reciprocals are given.")          
except:
    print("first loop completed")
for i in range(0, 6,1):

        
    try:
            
        sum += reciprocals[i]              
        if (i > 0):
                
            print(" + ")
            print("1/%.2lf", numbers[i])
              
            print(" = %lf\n", sum)
    except:
        print("Done")

