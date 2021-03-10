def DFS(x, y, number):

    if len(number) ==6:
        answer.add(number)
        return

    else:
        for i in range(4):
            r = x + dx[i]
            c = y + dy[i]

            if 0 <= r < 5 and 0 <= c < 5:
                DFS(r, c, number + str(board[r][c]))

board = [list(map(int, input().split())) for _ in range(5)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

number = ''
answer = set()

for i in range(5):
    for j in range(5):
        DFS(i, j, number)

print(len(answer))
