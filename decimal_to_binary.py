l1 = []
count = 0
def DecimaltoBinary(num):
    if num >= 1:
        DecimaltoBinary(num//2)
    a = num%2
    l1.append(a)
    print(a,end='')
    for j in range(l1):
        if i==1:
            count+=1
            
if __name__ == '__main__':
    val = int(input())
    DecimaltoBinary(val)
    print(l1)
    
