l,r,k= map(int,input().split())
c=0
while (l!=r+1):
    if l%k==0:
        c+=1
    l+=1    
print(c)