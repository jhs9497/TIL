n, m = map(int, input().split())

if 1 <= n <= 100 and 1 <= m <= 3:
    if m == 1:
        i = 1
        while i <= n:
            star = '*' * i
            print(star)
            i += 1

    elif m == 2:
        i = n
        while i >= 1:
            star = '*' * i
            print(star)
            i -= 1

    elif m == 3:
        i = 1
        N = n  # n을 쓰고 싶은데 while문에도 n을 써야하니 N으로 다시 담기
        while i <= n:
            j = 2*i -1
            star = (' '* (N-1)) + ('*' * j)
            print(star)
            i += 1
            N -= 1

else:
    print('INPUT ERROR!')