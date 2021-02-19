
idx = 0
for i in range(3):
    K = 5
    R = 0
    circle = [1, 6, 3, 7, 4]

    clock = int(input()) # 시계방향인지 반 시계 방향인지  # 1이면 역방향, 2면 정방향
    move = int(input()) # 몇번 돌리는지

# 시작은 circle[0] = 1

# 만약에 clock = 2 이고 move = 3이면 circle[3] 7이 나오겠지?
# K로 나머지 구하면 되는 부분인가 ?

# 만약에 clock = 1고 move = 3이면 circle[2] 3이 나온다. 역방향 대가리 깨진다 1, 15 = 1
# 걍 서클을 리버스로 하나 만들어놓자

    if clock == 2:
        if idx+move%K >= K:
            idx+move%K - K
        R = circle[idx + move%K]
        idx = idx + move%K
    else:
        if idx + K - move%K >= K:
            idx + K - move%K - K
        R = circle[idx + K - move%K]
        idx = idx + K - (move%K)

    print(R, idx)




