
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 시작점 찾는 함수
def search():
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                return i,j

# BFS 함수
def BFS(r, c):
    # 선형큐를 이용해서 작성을 해보자!
    Q = [0] * 1000000
    front = -1
    rear = 0
    Q[rear] = (r,c)

    dist = [[-1] * N for _ in range(N)]
    dist[r][c] = 0 # 첫 시작점 0 초기화

    while front != rear:
        front += 1
        cur_r, cur_c = Q[front]
        if maze[cur_c][cur_r] == '3':
            return dist[cur_r][cur_c] -1
        for i in range(4):
            nr = cur_r + dx[i]
            nc = cur_c + dy[i]

        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue
        if maze[nr][nc] != '1' and dist[nr][nc] == -1:
            dist[nr][nc] = dist[cur_r][cur_c] + 1
            rear += 1
            Q[rear] = (nr, nc)

    return 0

for tc in range(1, int(input())+1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]

    stR, stC = search()
    print('#{} {}'.format(tc, BFS(stR, stC)))