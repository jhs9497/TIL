for tc in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    # N : 자격을 얻은 사람의 수
    # M : M초동안
    # K : K개의 붕어빵 만들 수 있다.

    # 손님들이 몇초에 오는지
    customer = list(map(int, input().split()))

    # 손님들 시간 순서대로 정렬하고
    customer.sort()

    # 가장 늦게 오는 손님
    last_C = max(customer)

    # 우선 자격얻은 사람 수 보다 손님들이 많으면 impossible
    if N < len(customer):
        print('#{} Impossible'.format(tc))

    # 첫번째로 만드는 붕어빵보다 첫손님이 빨리오면
    elif customer[0] < M:
        print('#{} Impossible'.format(tc))


    else:  # 그렇지 않은 경우
        # 가장 늦게 오는 손님까지 for문을 돌리면서
        ans = 'Possible'
        count = 0
        for i in range(1, last_C + 1):
            if i % M == 0:  # M초의 배수이면
                count += K  # 카운트에 K개 추가
            if i in customer:  # 만약 i가 손님리스트에 있으면
                count -= 1  # 붕어빵 하나 먹기
                if count == -1:  # 남은 붕어빵이 없어서 마이너스가 되면
                    ans = 'Impossible'
                    break

        # 마지막엔 ans 출력
        print('#{} {}'.format(tc, ans))
