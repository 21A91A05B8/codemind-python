a,b=map(int,input().split())
s1=list(map(int,input().split()))
s2=list(map(int,input().split()))
for i in s1:
    if i not in s2:
        print(i,end=' ')
for i in s2:
    if i not in s1:
        print(i,end=' ')