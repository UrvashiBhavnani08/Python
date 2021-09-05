total=0
ele=0
mylist=[1,'orange','apple',2,3,4]
for item in mylist:
    mynewlist = [s for s in mylist if s.isdigit()]
    mynewlist.append(item)
print("\n")
print(mylist)
print(mynewlist)
for ele in range(0,len(mynewlist)):
    total = total + mynewlist[ele]
print("\n")
print(total)
