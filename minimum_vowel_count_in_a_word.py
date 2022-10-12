s=input().split()
v='aeiouAEIOU'
min=9
c=0
for i in s:
    c=0
    for j in i:
        if j in v :
            c+=1
    if(min>c):
        min=c
print(min)