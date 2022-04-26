N=int(input())
rev=0
temp=N
while(N):
    d=N%10
    N=N//10
    rev=rev*10+d
if(temp==rev):
    print("True")
else:
    print("False")
    