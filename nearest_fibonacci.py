n=int(input())
a=0
b=1
while(1):
    c=a+b
    if(c>n):
        break
    else:
        a=b
        b=c
k=c
c=c-a
if abs(n-k)<abs(n-c):
    print(k)
elif abs(n-k)>abs(n-c):
    print(c)
else:
    print(c,k)