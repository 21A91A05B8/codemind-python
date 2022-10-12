a,b=map(int,input().split())
s1=list(map(int,input().split()))
s2=list(map(int,input().split()))
c=0
k=set(s1)
l=set(s2)
for i in l:
    if i  not in k:
        c+=1
for i in k:
    if i not in l:
        c+=1
print(c)