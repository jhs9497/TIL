def DFS(x, y):
    visited  = [[0] * N for _ in range(N)]
    visited[x][y] = 1
    stack = [(x,y)]
    while stack:
        r, c = stack.pop()
        for i in range(4):
            dr = r + dx[i]
            dc = c + dy[i]
            if 0 <= dr < N and 0 <= dc < N:
                if MAP[r][c] > MAP[dr][dc]:
                    stack.append((dr,dc))
                    visited[dr][dc] = visited[r][c]+1

    return max(max(visited))

for tc in range(1, int(input())+1):
    N, K = map(int, input().split()) # N X N 지도, K -> 최대 공사 가능 깊이
    MAP = [list(map(int, input().split())) for _ in range(N)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 초기 봉우리 위치 찾기!
    # 우선 가장 큰 수 찾고
    Max_H = 0
    for i in range(N):
        for j in range(N):
            if Max_H < MAP[i][j]:
                Max_H = MAP[i][j]

    Max_list = []
    for i in range(N):
        for j in range(N):
            if MAP[i][j] == Max_H:
                Max_list.append((i,j))
    print(Max_list)

    result = []
    for k in range(K+1):
        for i in range(N):
            for j in range(N):
                MAP[i][j] = MAP[i][j] - k # MAP에서 k 빼주고
                for v in range(len(Max_list)):
                    (a,b) = Max_list[v]
                    result.append(DFS(a,b))
                MAP[i][j] = MAP[i][j] + k # 뻈던거 다시 초기화

    print('#{} {}'.format(tc, max(result)))


