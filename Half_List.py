n=int(input())
arr=list(map(int,input().split()))
c=n//2
for i in range(n-1,(n//2)-1,-1):
    print(arr[i],end=" ")
for i in range(n//2):
    print(arr[i],end=" ")