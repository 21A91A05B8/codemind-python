a,b=map(int,input().split())
s1=list(map(int,input().split()))
s2=list(map(int,input().split()))
k=set(s1)
l=set(s2)
c=0
for i in k:
    if i in l:
         c+=1
print(c)