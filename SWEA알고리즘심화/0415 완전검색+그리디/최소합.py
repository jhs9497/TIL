def find(row, col, midV):
    global min_
    if (row, col) == (N-1, N-1):
        if midV < min_:
            min_ = midV
        return

    if col+1 < N:
        find(row, col+1, midV+block[row][col+1] )
    if row+1 < N:
        find(row+1, col, midV+block[row+1][col])

for tc in range(1, int(input())+1):
    N = int(input())
    block = [list(map(int, input().split())) for _ in range(N)]
    min_ = 99**99
    find(0, 0, block[0][0])
    print('#{} {}'.format(tc, min_))
