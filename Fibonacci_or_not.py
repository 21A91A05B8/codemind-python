n=int(input())
a=0
b=1
while(1):
    c=a+b
    if(c==n):
        print("True")
        break
    if c>n:
        print("False")
        break
    a=b
    b=c
    
