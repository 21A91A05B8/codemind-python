a,b=map(int,input().split())
s1=list(map(int,input().split()))
s2=list(map(int,input().split()))
s3=[]
for i in s1:
    if i in s2:
        s3.append(i)
    if(s3.count(i)==1):
        print(i,end=' ')