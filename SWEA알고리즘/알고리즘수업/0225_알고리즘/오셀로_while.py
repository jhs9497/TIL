# 1: 돌 체크
def check(x, y, color):
    # 8방향 돌리기
    board[x][y] = color
    for i in range(8):
        r = x
        c = y
        # 한 발자국 갔을 때 돌이 1)빈공간도 아니고 2) 나랑 다른 색의 놓여진 돌이여야만 그 다음단계를 진행하면 된다.
        if 0 <= r < N and 0 <= c < N:
            count = 0
            door = True # while문 종료를 위한 변수
            while door == True and 0 <= r < N and 0 <= c < N:
                r = r + dx[i]
                c = c + dy[i]
                if door == True and 0 <= r < N and 0 <= c < N:
                    # door가 열려있는 동안이고 r, c 가 범위에 있다면
                    # 한 발자국 더 간 위치가 빈 공간이면
                    if board[r][c] == 0:
                        # 문 폐쇄
                        door = False
                    # 한 발자국 더 간 위치가 나랑 같은 색깔의 돌이면
                    elif board[r][c] == color:
                        for j in range(count+1):  #count된 수만큼
                            # 내 색으로 바꿔준다.
                            board[x+dx[i]][y+dy[i]] = color
                            x = x + dx[i]
                            y = y + dy[i]
                        # 문 폐쇄
                        door = False
                    # 한 발자국 더 간 위치가 나랑 다른 색깔의 '돌'이면
                    else:
                        count += 1 # count증가


for tc in range(1, int(input() ) +1):
    N, M = map(int, input().split()) # N은 판의 크기 M은 횟수

    # 오셀로 초기판 만들기
    board = [[0] *N for _ in range(N)]
    # 초기 말 놓기
    board[ N// 2 -1][ N// 2 -1] = 2
    board[ N//2][ N//2] = 2
    board[ N// 2 -1][ N//2] = 1
    board[ N//2][ N// 2 -1] = 1

    #     상 하 좌 우 우상향 좌상향 우하향 좌하향
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, 1, -1, 1, -1]


    for _ in range(M): # M번 만큼 반복할건데
        x, y, color = map(int, input().split())  # x좌표, y좌표 돌 색깔
        x -= 1
        y -= 1 # 나의 보드는 0부터 시작이므로 1씩 빼주고
        x, y = y, x

        if board[x][y] == 0:

            board[x][y] = color # 색칠해주고

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