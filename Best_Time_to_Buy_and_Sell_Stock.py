x=int(input())
l=list(map(int,input().split()))
c=0
k=[]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        k.append(l[j]-l[i])
for i in k:
    if i>0:
        c+=1
if(c==0):
    print("0")
else:
    print(max(k))