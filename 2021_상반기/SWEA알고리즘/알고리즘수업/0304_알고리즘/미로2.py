def search(x, y):
    miro[x][y] = 1 # 방문처리
    queue = []
    queue.append((x,y))

    while queue:
        x, y = queue.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < 16 and ny >= 0 and ny < 16:
                if miro[nx][ny] == 0:
                    miro[nx][ny] =1
                    queue.append((nx,ny))
                if miro[nx][ny] == 1:
                    continue
                if miro[nx][ny] == 3:
                    return 1

    return 0

for _ in range(1,11):
    tc = int(input())
    miro = [list(map(int, input())) for _ in range(16)]

    for i in range(16):
        for j in range(16):
            if miro[i][j] == 2:
                S = (i, j)
                break

    # 상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    a, b = S

    print('#{} {}'.format(tc, search(a, b)))