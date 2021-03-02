for tc in range(1, int(input())+1):
    N = int(input())
    # 복도를 경로로 색칠하자
    road = [0]*200
    for i in range(N):
        n, r = map(int, input().split())
        # 방번호를 수정해주자 위치는 그대로 두고 윗 줄 아랫줄 다 1~200 / 1~200 이도록
        if n % 2 == 0: # 짝수면
            n = n //2
        else: #홀수면
            n = n // 2 +1
        # r도 똑같이
        if r % 2 == 0:
            r = r// 2
        else:
            r = r //2 +1

        if n < r:
            for i in range(n, r+1):
                road[i] += 1
        else:
            for i in range(r, n+1):
                road[i] += 1
    # 겹치는 경로중 가장 빈번한놈 출력

    print('#{} {}'.format(tc, max(road)))