def perm(idx):
    if idx == N:
        print(sel)
        distance(sel)

        return
    for i in range(N):
        if check[i] == 0:
            sel[idx] = num_list[i]
            check[i] = 1
            perm(idx+1)
            check[i] = 0

def distance(sel):
    global count
    total = 0
    total += (abs(coordi[0][0] - coordi[sel[0]][0]) + abs(coordi[0][1] - coordi[sel[0]][1]))
    total += (abs(coordi[1][0] - coordi[sel[N-1]][0]) + abs(coordi[1][1] - coordi[sel[N-1]][1]))
    for i in range(len(sel)-1):
        total += (abs(coordi[i][0] - coordi[sel[i+1]][0]) + abs(coordi[i][1] - coordi[sel[i+1]][1]))
    if total < count:
        count = total


for tc in range(1, 2):
    N = int(input())
    I = list(map(int, input().split()))
    coordi = [[] for _ in range(N+2)]
    for i in range(0, len(I), 2):
        coordi[i//2].append(I[i])
        coordi[i//2].append(I[i+1])

    num_list = []
    for i in range(2, N+2):
        num_list.append(i)

    check = [0]*N
    sel = [0]*N

    count = 99999999999999999999
    perm(0)
    print(count)

