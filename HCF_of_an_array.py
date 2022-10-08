def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)
n=int(input())
arr=list(map(int,input().split()))
hcf=gcd(arr[0],arr[1])
for i in range(1,n):
    hcf =gcd(hcf,arr[i])
print(hcf)    