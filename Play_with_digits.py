n=int(input())
arr=list(map(int,input().split()))
sum=0
for i in arr:
    while(i):
        d=i%10
        i//=10
        sum+=d
print(sum)