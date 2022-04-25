num=int(input())   
d = 0
sum=0
n = num
while(num > 0):    
    d= num%10   
    sum = sum + d    
    num = num//10
if(n%sum == 0):    
    print("True")
else:    
    print("False")
