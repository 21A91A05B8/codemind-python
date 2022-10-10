grid = int(input())

if 1<=grid<=20:

    village = input()

    if 'HH' in village:

        print("NO")

    else:
        print("YES")

        print(village.replace('.',"B"))