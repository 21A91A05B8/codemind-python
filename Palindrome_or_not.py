def isPalindrome(s):
    return s==s[::-1]
s=input()
s=s.lower()
ans=isPalindrome(s)
if ans:
    print("True")
else:
    print("False")

    