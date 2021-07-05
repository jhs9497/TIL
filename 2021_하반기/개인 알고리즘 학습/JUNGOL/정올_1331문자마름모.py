N = int(input())

board = [[''] * (2*N-1) for _ in range(2*N-1)]
value = 65
i = N-1
x, y = 0, N-1
board[x][y] = chr(value)

while i > 0:
    dx = [1, 1, -1, -1]
    dy = [-1, 1, 1, -1]
    for j in range(4):
        for _ in range(i):
            x, y = x + dx[j], y + dy[j]
            if board[x][y] == '':
                if value == 90:
                    value = 65
                else:
                    value += 1

                board[x][y] = chr(value)

    i -= 1
    x, y =  x+1, y
    if value == 90:
        value = 65
    else:
        value += 1
    board[x][y] = board[x][y] = chr(value)

for i in range(len(board)):
    for j in range(len(board)):
        if board[i][j] == '':
            board[i][j] = ' '
        print(board[i][j], end=' ')
    print()
