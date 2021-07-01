n = int(input())

if n % 2 == 1 and 1 <= n <= 100:
    count = 1
    blank = 0
    for i in range(n):
        if i <= n // 2 -1 :
            star = ' ' * blank + '*' * count
            print(star)
            count += 2
            blank += 1

        else:
            star = ' ' * blank + '*' * count
            print(star)
            count -= 2
            blank -= 1


else:
    print('INPUT ERROR!')