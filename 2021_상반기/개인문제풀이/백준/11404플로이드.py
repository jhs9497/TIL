import sys

N = int(sys.stdin.readline()) # 도시의 개수 # input으로 했더니 안풀림
M = int(sys.stdin.readline()) # 버스의 개수

INF = 999999999

# 2차원 리스트를 만들고, 우선 모든 값을 무한으로 설정
graph = [[INF] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b, cost = map(int, input().split())
    # a에서 b로 가는 최소비용은 cost
    if cost < graph[a][b]:
        graph[a][b] = cost

for k in range(1, N+1): # k를 거치며
    for a in range(1, N+1): # a에서
        for b in range(1, N+1): # b로가는 경로중에서
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, N+1):
    for b in range(1, N+1):
        if graph[a][b] == INF or graph[a][b] == 0:
            print(0, end=" ")
        else:
            print(graph[a][b], end=" ")
    print()


