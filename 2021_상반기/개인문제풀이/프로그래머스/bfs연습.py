from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    # 현재 노드를 방문처리
    visited[start] = True
    # 큐가 빌때까지 반복
    while queue :
        # 큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        print(v, end=' ')
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]: # 첫바퀴에선 1
            if not visited[i]: # 방문하지 않았으면
                queue.append(i) # 큐에 삽입
                visited[i] = True # 방문처리


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7],
]

visited = [False] * 9
# 노드는 8번까지 있지만 인덱스 활용을 위해 +1해서 visted만들기

bfs(graph, 1, visited)