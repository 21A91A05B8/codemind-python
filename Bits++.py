c=0
k=0
for i in range(int(input())):
    n=input()
    if n=='X++' or n=='++X':
        c+=1
    else:
        c-=1
print(c)