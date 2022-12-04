n=int(input())
sum=0
while(n>0 or sum>9):
    if(n==0):
        n=sum
        sum=0
    else:
        sum=sum+n%10#8+3=11
        n=n//10#
print(sum)
