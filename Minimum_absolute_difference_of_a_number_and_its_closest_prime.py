def isprime(n):
    for i in range(2,n):
        if(n%i==0):
            return False
    else:
        return True
def difference(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    elif(isprime(n)):
        return 0
    a=0
    b=0
    n1=n+1
    while(True):
        if(isprime(n1)):
            a=n1
            break
        else:
            n1+=1
    n1=n-1
    while(True):
        if(isprime(n1)):
            b=n1
            break
        else:
            n1-=1
    diff1=a-n
    diff2=n-b
    return min(diff1,diff2)
n=int(input())
print(difference(n))