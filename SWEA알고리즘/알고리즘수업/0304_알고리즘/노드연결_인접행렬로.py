def BFS(S):
    Q = [(S, 0)]  # 시작점과 시작점~거기까지의 거리! 자기자신이니 0!
    # 방문체크!
    visited = [False] * (V+1)
    visited[S] = True

    while Q:
        v, dist = Q.pop(0)
        # 만약 내가 지금 서있는 위치가 도착점과 같다면
        if v == G:
            return dist # 거리 리턴

        for i in range(1, V+1):
            if adj_arr[v][i] == 1 and visited[i] == False:
                Q.append((i, dist+1))
                visited[i] = True

    return 0

################################################################

def BFS2(S):
    Q = [S] # 사이즈로 묶기 ?
    # 방문체크!
    visited = [False] * (V + 1)
    visited[S] = True

    dist = 0
    while Q:
        size = len(Q)
        for i in range(size): # 거리가 dist인 친구들만 돌린다
            v = Q.pop(0)
            if v == G: return dist

            for i in range(1, V+1):
                if not visited[i] and adj_arr[v][i]:
                    Q.append(i)
                    visited[i] = True
            dist += 1

    return 0

##########################################################################

for tc in range(1, int(input())+1):

    V, E = map(int, input().split())

    # 인접행렬 만들기
    adj_arr = [[0]*(V+1) for _ in range(V+1)]

    for i in range(E):
        a, b = map(int, input().split())
        # 인접행렬에 양방향 표시
        adj_arr[a][b] = 1
        adj_arr[b][a] = 1

    # 시작점, 끝점
    S, G = map(int, input().split())

    print('#{} {}'.format(tc, BFS(S)))