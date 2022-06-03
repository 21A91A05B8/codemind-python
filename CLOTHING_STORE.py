n=int(input())
a=list(map(int,input().split()))
k=0
for i in range(len(a)):
    c=0
    for j in range(i+1,len(a)):
        if(a[i]==a[j]):
            c+=1
    k+=c%2
print("%d"%k)