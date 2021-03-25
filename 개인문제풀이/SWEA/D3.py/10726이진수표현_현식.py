def check(N, M):
    if M == 0:
        return 'OFF'
    count = 0
    number = M
    while count < N:
        if number % 2 == 0:
            return 'OFF'
        number = number // 2
        count += 1
    return 'ON'


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    print('#{} {}'.format(tc, check(N, M)))
