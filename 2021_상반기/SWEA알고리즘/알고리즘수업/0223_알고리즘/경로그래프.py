def DFS(S):
    global result
    visited[S] = 1
    for next in range(1, v+1):
        if MyMap[S][next] and not visited[next]:
            if next == G_node:
                result = 1
                return
            DFS(next)

for tc in range(1, int(input())+1):
    v, e = map(int, input().split())
    MyMap = [[0]*(v+1) for _ in range(v+1)]
    visited = [0] * (v+1)  # stack
    for i in range(e):
        S, E = map(int, input().split())
        MyMap[S][E] = 1

    S_node, G_node = map(int, input().split())
    result = 0
    DFS(S_node)
    print('#{} {}'.format(tc, result))



