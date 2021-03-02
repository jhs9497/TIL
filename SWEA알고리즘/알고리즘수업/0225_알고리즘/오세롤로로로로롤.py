# 1: 돌 체크
def check(x, y, color):
    # 8방향 올리기
    for i in range(8):  # i = 0
        a = x + dx[i]
        b = y + dy[i]  # 일단 여기서 한 칸 간거고
        # x w (b) b w
        # 인덱스 체크
        for j in range(N):  # 일단 최대한 해보는거여
            if 0 <= a < N and 0 <= b < N:  # X가 범위 내에 있고
                if board[a][b] == 8:  # 이동한 상황에서 board[a][b]가 0이면 더 갈 필요가 없으므로 break
                    break

                elif board[a][b] == color:  # 뻗어나가다가 자기랑 같은 돌을 찾으면
                    if i == 0:  # 방향이 상 이었다면
                        for k in range(j):  # 1,2,3
                            if 0 <= x-k < N and 0 <= y < N:
                                board[x - k][y] = color  # 그 사이에 있는 돌들 같은색 돌로
                    elif i == 1:  # 방향이 하 였다면
                        for k in range(j):
                            if 0 <= x + k < N and 0 <= y < N:
                                board[x + k][y] = color
                    elif i == 2:  # 방향이 좌 였다면
                        for k in range(j):
                            if 0 <= x < N and 0 <= y-k < N:
                                board[x][y - k] = color
                    elif i == 3:  # 방향 우
                        for k in range(j):  # 0 1
                            if 0 <= x < N and 0 <= y+k < N:
                                board[x][y + k] = color
                    elif i == 4:  # 방향 우상향
                        for k in range(j):
                            if 0 <= x - k < N and 0 <= y+k < N:
                                board[x - k][y + k] = color
                    elif i == 5:  # 방향 좌상향
                        for k in range(j):
                            if 0 <= x - k < N and 0 <= y-k < N:
                                board[x - k][y - k] = color
                    elif i == 6:  # 방향 우하향
                        for k in range(j):
                            if 0 <= x + k < N and 0 <= y +k < N:
                                board[x + k][y + k] = color
                    elif i == 7:  # 좌하향
                        for k in range(j):
                            if 0 <= x + k < N and 0 <= y-k < N:
                                board[x + k][y - k] = color

                else:  # 이동한 상황에서 돌이 자기랑 다른돌이면
                    a = a + dx[i]
                    b = b + dy[i]


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())  # N은 판의 크기 M은 횟수

    # 오셀로 초기판 만들기
    board = [[8] * N for _ in range(N)]
    # 초기 말 놓기
    board[N // 2 - 1][N // 2 - 1] = 2
    board[N // 2][N // 2] = 2
    board[N // 2 - 1][N // 2] = 1
    board[N // 2][N // 2 - 1] = 1

    #     상 하 좌 우 우상향 좌상향 우하향 좌하향
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, 1, -1, 1, -1]

    for _ in range(M):  # M번 만큼 반복할건데
        x, y, color = map(int, input().split())  # x좌표, y좌표 돌 색깔
        x -= 1
        y -= 1  # 나의 보드는 0부터 시작이므로 1씩 빼주고
        x, y = y, x

        if board[x][y] == 8:
            board[x][y] = color  # 색칠해주고

            check(x, y, color)  # check함수에 보내서 x, y 체크해주기
        for i in board:
            print(*i)
    # M번의 체크가 끝났으면
    black = 0
    white = 0

    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                black += 1
            if board[i][j] == 2:
                white += 1

    print('#{} {} {}'.format(tc, black, white))