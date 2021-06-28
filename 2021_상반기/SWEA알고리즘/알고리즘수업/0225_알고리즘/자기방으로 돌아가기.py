for tc in range(1, int(input())+1):
    N = int(input())
    now_room = []
    return_room = []
    for i in range(N):
        n, r = map(int, input().split())
        # 방번호를 수정해주자 위치는 그대로 두고 윗 줄 아랫줄 다 1~200 / 1~200 이도록
        if n % 2 == 0: # 짝수면
            n = n //2
        else: #홀수면
            n = n // 2 +1
        now_room.append(n)  # 리스트에 추가
        # r도 똑같이
        if r % 2 == 0:
            r = r// 2
        else:
            r = r //2 +1
        return_room.append(r)
    # 복도를 경로로 색칠하자
    road = [0] * 200

    for i in range(N):
        for j in range(now_room[i], return_room[i]+1):
            road[j] += 1
    # 겹치는 경로중 가장 빈번한놈 출력
    ans = max(road)

    print('#{} {}'.format(tc, ans))



