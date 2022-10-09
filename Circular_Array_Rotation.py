a,b,c=map(int,input().split())
arr=list(map(int,input().split()))
for i in range(b):
    t=arr[a-1]
    for j in range(a-1,0,-1):
        arr[j]=arr[j-1]
    arr[0]=t
for i in range(c):
    v=int(input())
    print(arr[v])