s=input()
s=list(s.split())
v='aeiouAEIOU'
t='qwrtyplkjhgfdszxcvnm'
c=0
for i in s:
    if(i[0] in v and i[len(i)-1] in t):
        c+=1
print(c)
    