n=int(input())
arr=list(map(int,input().split()))
sum=sum(arr)
l=len(arr)
avg=sum//l
c=0
for i in range (0,len(arr)):
    if(avg>=arr[i]):
        c+=1
print(c)        
