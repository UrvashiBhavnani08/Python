import array as arr
a = arr.array('i',[0,1,2,3,4,5,6,7,8,9,10,11,12])
for i in range(0,10):
    print(a[i],end=" ")
print("\n")
num = int(input("Enter which number you want to search through LINEAR SEARCH : "))
def linear_search(a,l1,num):
    for i in range(0,length):
        beg = a[0]
        end = a[12]
        mid = (a[0] + a[12])/2
        if (num <= mid):
            beg = a[0]
            end = mid
            mid = (beg + end)/2
            if (num <= mid):
                beg = a[0]
                end = mid
                mid = (beg+end)/2
    return -1
#print(a.index(6))
#print(len(a))
length = len(a)
result = linear_search(a,length,num)
if (result == -1):
    print("Sorry not found.")
else:
    print("Number is at index: ",result)
#print(a[0])  


    
