def check(x, y):
    global board
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    zero_count = 0
    if x == 0 or x == 99 or y == 0 or y == 99:
        zero_count += 1
    for i in range(4):
        if 0 <= x+dx[i] <= 99 and 0 <= y+dy[i] <= 99:
            if board[x+dx[i]][y+dy[i]] == 0:
                zero_count += 1

    return zero_count

board = [[0]*100 for _ in range(100)]

N = int(input())

for _ in range(N):
    x, y = map(int, input().split())
    x, y = x-1, y-1
    for i in range(x, x+10):
        for j in range(y, y+10):
            board[i][j] += 1

count = 0
for a in range(100):
    for b in range(100):
        if board[a][b] != 0:
            x = check(a, b)
            count += x

print(count)