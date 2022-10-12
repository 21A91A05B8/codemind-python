s=input().split()
v='aeiouAEIOU'
max=0
c=0
for i in s:
    c=0
    for j in i:
        if j in v :
            c+=1
        if(max<c):
            max=c
print(max)