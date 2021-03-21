for tc in range(1, int(input())+1):
    D, L, N = map(int, input().split())
    n = 0
    total = 0
    while n < N:
        total += D*(1+(n*L*0.01))
        n += 1

    print('#{} {}'.format(tc, int(total)))