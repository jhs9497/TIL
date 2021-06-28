import copy

def DFS(shark_x, shark_y):
    first_x = shark_x
    first_y = shark_y  # 맨 초기 아기상어 위치 저장
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = []
    queue.append((shark_x, shark_y))
    Space = copy.deepcopy(space)  # 이 함수 내부에서만 돌릴 Space 만들어주고
    Space[shark_x][shark_y] = 10  # 카운팅을 위해 1 대신 10으로
    while queue:
        shark_x, shark_y = queue.pop(0)
        for i in range(4):
            x = shark_x + dx[i]
            y = shark_y + dy[i]

            if 0 <= x < N and 0 <= y < N:

                if Space[x][y] > size: # 만약 만난 물고기가 아기상어보다 크다면
                    continue

                if Space[x][y] <= size : # 만약 만난 물고기가 아기상어보다 같거나 작다면
                    Space[x][y] = 10 + Space[shark_x][shark_y] # 방문처리 하고
                    queue.append((x, y)) # 큐에 추가
    fish_idx = []
    for i in range(N):
        for j in range(N):
            if Space[i][j] < 10:
                Space[i][j] = -1
            else:
                Space[i][j] = Space[i][j] // 10
                if i, j != first_x, first_y: # 만약 아기상어의 초기위치랑 다르다면
                    fish_idx.append((i,j))



    return Space

size = 2
N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]
sec_ = DFS(5,5)
print(DFS(2,2))