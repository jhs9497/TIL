from collections import deque

n, m = map(int, input().split())

graph = [list(map(int, input())) for _ in range(n)]

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y)) # 튜플형태로 ?
    # 큐가 빌때까지 반복
    while queue:
        x, y = queue.popleft()  # == queue.pop(0) 덱이 리스트보다 메모리 효율 좋아서 덱 사용
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문 하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1 # 처음 가는 경로마다 + 1 씩
                queue.append((nx, ny))  # 처음 가본 경로면 큐에 추가

    # while문이 끝나고 목표점인 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n-1][m-1]

# BFS를 수행한 결과 출력
print(bfs(0, 0))  # 출발점이 0,0인 경우임

for i in range(5):
    print(*graph[i])