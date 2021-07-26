def check(x, y):
    global board
    # 상하좌우 움직일 방향키 ?
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    # 리턴으로 내보낼 0의 갯수
    zero_count = 0
    # 아래의 경우 보드판의 맨 가장자리에 속한다는 뜻이므로 zero_count를 1추가하고 시작
    if x == 0 or x == 99 or y == 0 or y == 99:
        zero_count += 1
    # 4방향으로 확인하면서
    for i in range(4):
        # 보드판 범위를 초과하지 않는 선에서
        if 0 <= x+dx[i] <= 99 and 0 <= y+dy[i] <= 99:
            # 0의 갯수 카운팅
            if board[x+dx[i]][y+dy[i]] == 0:
                zero_count += 1

    return zero_count

# 0으로 이루어진 100 X 100 보드판 만들기
board = [[0]*100 for _ in range(100)]

N = int(input())

# 보드판에 입력받을 사각형 갯수만큼 for문 돌리면서 0대신 1로 칠해주기
for _ in range(N):
    x, y = map(int, input().split())
    x, y = x-1, y-1
    for i in range(x, x+10):
        for j in range(y, y+10):
            board[i][j] = 1


# 보드판을 한 번 더 돌면서
count = 0
for a in range(100):
    for b in range(100):
        # 0이 아닌경우! ( 사각형에 속하는 경우 )
        if board[a][b] != 0:
            # 테두리에 해당하는지 체크하는 check함수에 인덱스 보내기
            x = check(a, b)
            # return 값을 맨 위 count에 더해가주기
            count += x

print(count)