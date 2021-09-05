dict1 = {'Name' : 'Reema' , 'Sport' : 'Basketball'}
dict2 = {'Age' : '18', 'Course' : 'Mathematics', 'Rank' : '1'}
dict3 = {'Hobby' : 'Painting'}
dict4 = dict(**dict1, **dict2, **dict3)
print(dict4)
