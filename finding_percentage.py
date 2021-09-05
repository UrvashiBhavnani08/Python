n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
total=0
l1 = student_marks[query_name]
for i in range(0,len(l1)):
    total = total+l1[i]

average = total/3
print('%.2f'%average)

