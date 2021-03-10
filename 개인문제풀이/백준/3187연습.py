N, M = map(int, input().split())

Yard = [input() for _ in range(N)]

New_Yard = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if Yard[i][j] =='v':
            New_Yard[i][j] = 1
        if Yard[i][j] =='k':
            New_Yard[i][j] = 2