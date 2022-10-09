n=int(input())
a=list(map(int,input().split()))
b=[]
p=1
for i in range(len(a)):
    p=p*a[i]
for i in range(len(a)):
    b.append(p)
for i in range(len(a)):
    b[i]=p//a[i]
print(*b)