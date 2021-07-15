
board = [[0]*100 for _ in range(100)]

N = int(input())

for _ in range(N):
    x, y = map(int, input().split())
    x, y = x-1, y-1
    for i in range(x, x+10):
        for j in range(y, y+10):
            board[i][j] = 1

count = 0
for a in range(100):
    for b in range(100):
        if board[a][b] == 1:
            count += 1

print(count)