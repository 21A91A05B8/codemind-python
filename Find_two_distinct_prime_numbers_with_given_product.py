def isprime(n):
    for i in range(2,n):
        if(n%i==0):
            return False
    else:
        return True
        
def product(n):
    c=0
    for i in range(1,n+1):
        for j in range(i+1,n):
            if(isprime(i) and isprime(j)):
                if((i*j)==n):
                    print(i,j,end=" ")
                    c+=1
                    break
            
                else:
                    continue
    if(c==0):
        print("-1")
    
            
                
n=int(input())
(product(n))
