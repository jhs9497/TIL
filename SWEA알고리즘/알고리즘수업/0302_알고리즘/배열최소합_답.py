def per(k):
    global minV
    if k == N:
        sumV = 0
        for i in range(N):
            sumV += BRD[i][sel[i]]

        if minV > sumV:
            minV = sumV

    for i in range(N):

        if not visited[i]:
            sel[k] = i
            visited[i] = True
            per(k+1)
            visited[i] = False

for tc in range(1, int(input())+1):
    N = int(input())
    BRD = [list(map(int, input().split())) for _ in range(N)]
    sel = [-1] * N
    visited = [False] * N
    minV = 99999999999999

    per(0)

    print('#{} {}'.format(tc, minV))