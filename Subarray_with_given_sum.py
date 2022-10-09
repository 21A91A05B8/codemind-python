x=int(input())
for i in range(x):
    y,z=map(int,input().split())
    l=list(map(int,input().split()))
    c=0
    k=0
    for i in range(1,len(l)+1):
        for j in range(i-1,len(l)):
            k=k+l[j]
            if(k==z):
                c+=1
                print(i,j+1)
                break
        k=0
        if(c>0):
            
            break
    if(c==0):
        print("-1")