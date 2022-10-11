n=int(input())
arr=list(map(int,input().split()))
c=[]
d=[]
for i in arr:
    if(i%2==0):
        c.append(i)
    elif(i%2!=0):
        d.append(i)
i=0
j=0
while(i<len(c) or j<len(d)):
     
    if(j<len(d)):
        print(d[j],end=' ')
    j+=1
    if(i<len(c)):
        print(c[i],end=' ')
    i+=1    
if(n%2!=0):
    print("0")
        