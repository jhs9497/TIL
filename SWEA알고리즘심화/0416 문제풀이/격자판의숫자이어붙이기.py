def check(x, y, answer):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    if len(answer) == 7:
        result.add(answer)
        return

    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if 0 <= new_x < 4 and 0 <= new_y < 4 and len(answer) + 1 <= 7:
            check(new_x, new_y, answer+board[new_x][new_y])

for tc in range(1, int(input())+1):
    board = [input().split() for _ in range(4)]
    result = set()
    for i in range(4):
        for j in range(4):
            check(i,j, board[i][j])

    print('#{} {}'.format(tc, len(result)))