N = int(input())

square = [[0] * N for _ in range(N)]

dx = [1, -1, 0, 1]
dy = [0, 1, 1, -1]
value = 1
x, y = 0, 0
square[x][y] = value

for _ in range(N-1):
    for i in range(4):
        if i == 0:
            value += 1
            if 0 <= x+dx[0] < N and 0 <= y+dy[0] < N:
                x = x + dx[0]
                y = y + dy[0]
                square[x][y] = value
            else:
                x = x + dx[2]
                y = y + dy[2]
                square[x][y] = value

        elif i == 1:
            while 0 <= x + dx[1] < N and 0 <= y + dy[1] < N:
                value += 1
                x = x + dx[1]
                y = y + dy[1]
                square[x][y] = value

        elif i == 2:
            value += 1
            if 0 <= x+dx[2] < N and 0 <= y+dy[2] < N:
                x = x + dx[2]
                y = y + dy[2]
                square[x][y] = value
            else:
                x = x + dx[0]
                y = y + dy[0]
                square[x][y] = value

        elif i == 3:
            while 0 <= x + dx[3] < N and 0 <= y + dy[3] < N:
                value += 1
                x = x + dx[3]
                y = y + dy[3]
                square[x][y] = value

for row in square:
    print(*row)

