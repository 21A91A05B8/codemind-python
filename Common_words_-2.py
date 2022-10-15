s1=input().split()
s2=input().split()
c=0
for i in s1:
    if s1.count(i)==1:
        if i in s2:
            if(s2.count(i)==1):
                c+=1
print(c)