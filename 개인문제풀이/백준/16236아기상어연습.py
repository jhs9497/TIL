import copy

def fish_bfs(shark_x, shark_y, a, b):
    sample = copy.deepcopy(space)  # 이 함수 내부에서만 돌릴 Space 만들어주고
    visited = [[False] * N for _ in range(N)]
    queue = [(shark_x, shark_y)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    sample[shark_x][shark_y] = 0 # 나자신 0으로 초기화
    visited[shark_x][shark_y] = True # 방문처리
    while queue:
        shark_x, shark_y = queue.pop(0)
        for i in range(4):
            x = shark_x + dx[i]
            y = shark_y + dy[i]
            if 0 <= x < N and 0 <= y < N:
                if sample[x][y] <= size and visited[x][y] == False:
                    sample[x][y] = sample[shark_x][shark_y] + 1
                    visited[x][y] = True
                    queue.append((x,y))

    return sample[a][b]



N = int(input())

size = 2

shark_x, shark_y = 5, 5

space = [list(map(int, input().split())) for _ in range(N)]

fish = []  # 먹을 수 있는 물고기 리스트 뽑기
for i in range(N):
    for j in range(N):
        if space[i][j] < size and space[i][j] != 0:  # 0이 아니면서 아기상어보다 작은 물고기 찾기
            fish.append(space[i][j])

fish_idx = []
for i in range(N):
    for j in range(N):
        if space[i][j] in fish:  # 만약 먹을 수 있는 물고기에 해당하면
            # 현재 아기상어와의 거리도 함수로 구해서 물고기 리스트에 추가
            d = fish_bfs(shark_x, shark_y, i, j)
            fish_idx.append((d, i, j))

print(fish_idx)
