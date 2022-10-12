n=int(input())
arr=list(map(int,input().split()))
rev=0
for i in arr:
    rev=0
    while(i):
        d=i%10
        i//=10
        rev=rev*10+d
    print(rev,end=' ')