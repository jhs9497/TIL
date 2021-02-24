def paper(x):
    if x == 1:
        return 1

    if x % 2 == 0: # 짝수이면
        return (paper(x-1) *2) + 1

    else: # 홀수이면
        return (paper(x-1) *2) - 1

for tc in range(1, int(input())+1):
    X = int(input())
    x = X // 10

    print('#{} {}'.format(tc, paper(x)))

