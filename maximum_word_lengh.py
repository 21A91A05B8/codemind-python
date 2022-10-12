s=input().split()
max=0
for i in s:
    if(max<len(i)):
        max=len(i)
print(max)