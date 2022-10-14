n=int(input())
for i in range(2**n):
    k=bin(i)
    k=k[2::]
    k=list(k)
    k=k[::-1]
    f=n-len(k)
    for i in range(f):
        k.append(0)
    k=k[::-1]
    for i in range(n):
        if k[i]=='0':
            k[i]=0
        elif k[i]=='1':
            k[i]=1
    for i in range(n):
        print(k[i],end="")
    print()