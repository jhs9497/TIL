Test_case = int(input())

for tc in range(1, Test_case+1):
    N, M = map(int, input().split())
    number = list(map(int, input().split()))

    # N = 전체길이
    # M = 이웃범위

    max_number = 0
    min_number = 99999999
    for i in range(N+1-M):  # i를 그냥 맨 처음 인덱스로 생각합시다
        sum_number = 0
        for j in range(M): # 0, 1, 2, 3, M
            sum_number += number[i+j]

        if max_number < sum_number:  # 왜 < 했을때는 안됐을까 ?
            max_number = sum_number
        if min_number > sum_number:  # 왜 > 했을떄는 안됐을까 ? 2
            min_number = sum_number

    answer = max_number - min_number

    print('#{} {}'.format(tc, answer))

