s=input()
s=s.split(" ")
vowel='aeiou'
c=1
a=[]
for i in s:
    if i[0] in vowel:
        x=i+'ma'+("a"*c)
    
    else:
        x=i[1::]+i[0]+'ma'+("a"*c)
    c+=1
    a.append(x)
for i in a:
    print(i,end=' ')