n=int(input())
sum=0
sum1=0
a=list(map(int,input().split()))
for i in range(n):
    if(i%2==0):
        sum+=a[i]
    else:
        sum1+=a[i]
diff= sum-sum1
if(diff==0):
    print('YES')
else:
    print('NO')