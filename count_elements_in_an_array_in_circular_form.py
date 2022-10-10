n=int(input())
arr=list(map(int,input().split()))
arr.append(arr[0])
arr.append(arr[1])
c=0
n=n+2
for i in range(0,n-2):
    if(arr[i]%2==0) and (arr[i+2]%2!=0):
        c+=1
    elif(arr[i]%2!=0) and (arr[i+2]%2==0):
        c+=1
print(c)
        
    