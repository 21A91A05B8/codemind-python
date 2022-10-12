n=int(input())
arr=input().split()
c=[]
for i in arr:
    c.append(len(i))
m=max(c)
for i in arr:
    if(len(i)==m):
        print(i,end=' ')