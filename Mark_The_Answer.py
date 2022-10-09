a,b=map(int,input().split())
c=list(map(int,input().split()))
x=0
z=0
for i in c:
    if i>b:
        x+=1
    else:
        if x<=1:
            z+=1
        else:
            break
print(z)