def dfs(index, now):
    global min_
    if index == N:
        if now >= H:
            if now <= min_:
                min_ = now
    else:
        visited[index] = 1
        dfs(index+1, now + employee[index] * visited[index])
        visited[index] = 0
        dfs(index+1, now + employee[index] * visited[index])


for tc in range(1, int(input())+1):
    N, H = map(int, input().split())
    employee = list(map(int, input().split()))
    visited = [0]*N
    min_ = 99999999999999
    dfs(0, 0)
    print('#{} {}'.format(tc, min_-H))


