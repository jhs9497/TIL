dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def BFS(r, c):
    Q = [(r,c)]

    while Q:
        x, y = Q.pop(0)
        for i in range(4):
            nr = x + dr[i]
            nc = y + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= N :
                continue

            # 서있는 위치가 도착지점인가 ?
            if maze[nr][nc] == 3:
                return 1

            # 갈 수 있는 자리라면
            if maze[nr][nc]  == 0:
                Q.append((nr,nc))
                maze[nr][nc] = 1 # 방문체크

    return 0

for _ in range(1, 11):
    tc = int(input())
    N = 16

    maze = [list(map(int, input())) for _ in range(N)]

    # 시작점을 찾아서 출발해야 하므로
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sR = i
                sC = j
                maze[i][j] = 1

    print('#{} {}'.format(tc, BFS(sR,sC)))