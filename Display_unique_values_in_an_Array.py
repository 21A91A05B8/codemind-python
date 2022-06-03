n=int(input())
a=list(map(int,input().split()))
c=0
k=0
for i in range(len(a)):
    c=0
    for j in range(len(a)):
        if(i!=j):
            if(a[i]==a[j]):
                c+=1
                
    if(c==0):
        print(a[i],end=' ')
        k+=1
if(k==0):
    print("-1")
        
    