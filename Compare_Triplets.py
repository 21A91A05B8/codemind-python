l=list(map(int,input().split()))
m=list(map(int,input().split()))
a=0
b=0
for i in range(len(l)):
    if l[i]>m[i]:
        a+=1
    if(l[i]<m[i]):
        b+=1
    
print(a,end=" ")
print(b)