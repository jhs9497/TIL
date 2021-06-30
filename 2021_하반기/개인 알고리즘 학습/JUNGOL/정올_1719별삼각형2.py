n, m = map(int, input().split())

if n % 2 == 0 or n < 1 or n > 100 or m < 1 or m > 4:
    print('INPUT ERROR!')

else:
    if m == 1:
        d = 'up'
        i = 1
        for _ in range(n):
            star = '*' * i
            print(star)
            if i == (n//2) +1:
                d = 'down'

            if d == 'up':
                i += 1
            else:
                i -= 1

    elif m == 2:
        i_d = 'up'
        N_d = 'down'
        i = 1
        N = n // 2
        for _ in range(n):
            star = ' '*N + '*'*i
            print(star)

            if i == (n//2) +1:
                i_d = 'down'

            if i_d == 'up':
                i += 1
            else:
                i -= 1

            if N == 0:
                N_d = 'up'

            if N_d == 'up':
                N += 1
            else:
                N -= 1

    elif m == 3:
        i = (n // 2) + 1
        i_d = 'down'
        N = 0
        N_d = 'up'
        for _ in range(n):
            star = ' '* N + '*' * (2*i -1)
            print(star)
            if i == 1:
                i_d = 'up'

            if i_d == 'up':
                i += 1
            else:
                i -= 1

            if N == n // 2:
                N_d = 'down'

            if N_d == 'up':
                N += 1
            else:
                N -= 1

    elif m == 4:
        i = n // 2 + 1
        i_d = 'down'
        N = 0
        N_d = 'up'

        for _ in range(n):
            star = ' '* N + '*'*i
            print(star)

            if i == 1:
                i_d = 'up'

            if i_d == 'up':
                i += 1
            else:
                i -= 1

            if N < n // 2:
                N += 1
