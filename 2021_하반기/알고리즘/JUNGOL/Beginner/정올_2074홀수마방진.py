N = int(input())

board = [[0]*N for _ in range(N)]

value = 1
x, y = 0, N//2
board[x][y] = value

while value < N**2:
    if value % N == 0:
        x += 1
        value += 1
        board[x][y] = value

    else:
        value += 1
        if 0 <= x-1 < N and 0 <= y-1 < N:
            x -= 1
            y -= 1
            board[x][y] = value

        elif x-1 < 0 and 0 <= y-1 < N:
            x = N-1
            y -= 1
            board[x][y] = value

        elif 0 <= x-1 < N and y-1 < 0:
            x -= 1
            y = N-1
            board[x][y] = value

for i in board:
    print(*i)

