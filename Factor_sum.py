arr=list(map(int,input().split(',')))
d=0
s=[]
c=0
for i in arr:
    d=0
    for j in range(1,i+1):
        if(i%j==0):
            d=d+j
    if d in arr:
        s.append(i)
        c+=1
if(c==0):
    print("-1")
else:
    s=sorted(s)
    print(*s)