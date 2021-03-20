def search(x, y):
    visited = [[-1]*N for _ in range(M)]
    visited[x][y] = 1
    stack = []
    stack.append((x,y))
    while stack:
        x, y = stack.pop()
        for i in range(4):
            dr = x + dx[i]
            dc = y + dy[i]
            if 0 <= dr < M and 0 <= dc < N:
                if site[dr][dc] == '.' and visited[dr][dc] == -1:
                    stack.append((dr,dc))
                    visited[dr][dc] = visited[x][y] + 1


    (z, k) = (0, 0)
    K = 9999999
    for i in range(N):
        if visited[M-1][i] != -1 and visited[M-1][i] < K:
            K = visited[M-1][i]
            (z, k) = (M-1, i)

    if (z, k) == (0, 0):
        return []

    stack_2 = []
    stack_2.append((z,k))
    road = []
    road.append((z,k))
    while stack_2:
        z, k = stack_2.pop()
        for i in range(4):
            new_z = z + dx[i]
            new_k = k + dy[i]
            if 0 <= new_z < M and 0 <= new_k < N:
                if visited[z][k] == visited[new_z][new_k] +1:
                    road.append((new_z, new_k))
                    stack_2.append((new_z, new_k))
                    break

    return road

N, M = map(int, input().split())

site = [input() for _ in range(M)]

dx = [-1, 1, 0, 0]
dy = [0, 0 , -1, 1]

sample = []

for a in range(M):
    for b in range(N):
        if site[a][b] =='c':
            sample.append(search(a,b))


standard_cnt = 99999999
standard = []
for i in range(len(sample)):
    if standard_cnt > len(sample[i]):
        standard = sample[i]

if standard:
    count = 0
    for i in range(len(standard)-1):
        if standard[i][1] != standard[i+1][1]:
            count += 1

    print(count)
else:
    print('-1')