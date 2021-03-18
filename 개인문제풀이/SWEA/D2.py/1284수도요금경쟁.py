for tc in range(1, int(input())+1):
    P, Q, R, S, W = map(int, input().split())
    # A사: 1리터당 P원
    # B사: 기본요금 Q원 + R초과부턴 1리터당 S원 추가
    A = P * W
    B = Q
    if R > W:
        extra = 0
    else:
        extra = (W-R) * S
    print(extra)
    B += extra

    if A > B:
        print('#{} {}'.format(tc, B))
    else:
        print('#{} {}'.format(tc, A))