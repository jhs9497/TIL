def search(S, G, visited):
    queue = []
    queue.append(S)
    while queue:
        x = queue.pop(0)
        for i in road[x]:
            if visited[i] == 0:
                visited[i] = visited[x] + 1
                queue.append(i)
    return visited[G]


for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    # V개의 노드
    # E개의 간선정보
    info = [[0]]+[list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    visited = [0] * (V + 1)  # 방문 체크 이자 count

    road = [[] for _ in range(V+1)]

    for i in range(1, len(info)):
        road[info[i][0]].append(info[i][1])
        road[info[i][1]].append(info[i][0])
    # 내가 하고 싶은거
    #[[], [3, 4], [3, 5], [1, 2], [1, 6], [2], [4]]


    print('#{} {}'.format(tc, search(S, G, visited)))