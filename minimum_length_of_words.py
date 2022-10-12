s=input().split()
min=100
for i in s:
    if(min>len(i)):
        min=len(i)
print(min)