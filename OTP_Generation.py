x=int(input())
k=[]
x=str(x)
for i in x:
    if int(i)%2==0:
        pass
    else:
        i=int(i)
        k.append(i*i)
for i in k:
    print(i,end="")