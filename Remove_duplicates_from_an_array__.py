a=int(input())
b=[]
arr=list(map(int,input().split()))
for i in arr:
    if i not in b:
        b.append(i)
for i in b:
    print(i,end=" ")
