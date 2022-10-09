n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    b=i**0.5
    c=int(b)
    if c==b:
        s+=i
print(s)