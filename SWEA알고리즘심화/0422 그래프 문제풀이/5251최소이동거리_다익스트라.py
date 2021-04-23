import heapq

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 거리는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
        dist, now = heapq.heappop(q) # heapq 자료구조기 때문에 자동으로 최소값이 빠져나옴
        if distance[now] < dist: # 만약 지금 뽑은 dist가 저장되어있는 값보다 크면 걍 넘어가고
            continue
        else:
            # 현재 노드와 연결된 다른 인접한 노드를을 확인
            for i in graph[now]:
                cost = dist + i[1]
                # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

for tc in range(1, int(input())+1):

    n, m = map(int, input().split())
    start = 0
    INF = int(1e9)
    graph = [[] for _ in range(n+1)]
    # 최단 거리 테이블은 모두 무한으로 만들어두기
    distance = [INF] * (n + 1)

    for _ in range(m):
        x, y, z = map(int, input().split())
        # X번 노드에서 Y번 노드로 가는 비용은 Z라는 의미
        graph[x].append((y, z))

    # 다익스트라 알고리즘 수행
    dijkstra(start)

    # 도달할 수 있는 노드의 개수
    count = 0
    # 도달할 수 있는 노드 중에서, 가장 멀리 있는 노드와의 최단 거리
    max_distance = 0
    for d in distance:
        # 도달 할 수 있는 노드면 무한대가 아닐 것
        if d != INF:
            count += 1
            max_distance = max(max_distance, d)

    print('#{} {}'.format(tc, distance[-1]))
