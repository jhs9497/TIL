def DFS(X):
    visited = [False] * 100
    visited[X] = True
    stack = []
    stack.append(X)
    while stack:
        now = stack.pop()
        for i in range(len(con[now])):
            if visited[con[now][i]] == False:
                visited[con[now][i]] = True
                stack.append(con[now][i])
                if con[now][i] == 99:
                    return 1
    return 0


for _ in range(1, 11):
    tc, N = map(int, input().split())
    info = list(map(int, input().split()))
    con = [[] for _ in range(100)]
    for i in range(0, len(info), 2):
        con[info[i]].append(info[i+1])

    print('#{} {}'.format(tc, DFS(0)))