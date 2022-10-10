s=input()

vowels='aeiouAEIOU'
Digits='0123456789'
Consonants='bcdfghjklmnpqrstwvxyzBCDFGHJKLMNPQRSTVWXYZ'
v=0
c=0
d=0
w=0
for i in s:
    if i in vowels:
        v+=1
    elif i in Consonants:
        c+=1
    elif i in Digits:
        d+=1
    elif i==' ':
        w+=1
print("Vowels:",v)
print("Consonants:",c)
print("Digits:",d)
print("White spaces:",w)

        