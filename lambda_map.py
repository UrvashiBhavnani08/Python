
cube = lambda x: x ** 3
def fibonacci(n):
    count=0
    n1,n2=0,1
    l1=[0,1]
    for i in range(2,n):
        l1.append(l1[i-1]+l1[i-2])
    return(l1[0:n])
    
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube,fibonacci(n))))
