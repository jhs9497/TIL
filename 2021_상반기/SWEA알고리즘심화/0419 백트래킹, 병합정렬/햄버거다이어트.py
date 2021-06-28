def dfs(idx, score, kcal):
    global select
    if idx == N:
        if kcal <= limit:
            if score >= select:
                select = score

    else:
        visited[idx] = 1
        dfs(idx+1, score + data[idx][0] * visited[idx], kcal + data[idx][1] * visited[idx])
        visited[idx] = 0
        dfs(idx + 1, score + data[idx][0] * visited[idx], kcal + data[idx][1] * visited[idx])


for tc in range(1, int(input())+1):
    N, limit = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    select = 0
    dfs(0, 0, 0)
    print('#{} {}'.format(tc, select))