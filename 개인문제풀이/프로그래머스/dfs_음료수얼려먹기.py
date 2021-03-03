
# DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        graph[x][y] = 1 # 방문처리
        # 상 하 좌 우 위치들 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    else:
        return False



n,m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기 (얼음판)
graph = [list(map(int, input())) for _ in range(n)]

# 모든 노드(위치)에 대하여 음료수 탐색

count = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 dfs 수행
        if dfs(i, j) == True:
            count += 1

print(count)

