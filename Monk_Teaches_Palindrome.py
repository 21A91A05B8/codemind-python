n=int(input())
while n:
    s=str(input())
    if s==s[::-1]:
        if len(s)%2:
            print('YES ODD')
        else:
            print('YES EVEN')
    else:
        print('NO')
    n-=1