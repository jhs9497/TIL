N = int(input())

board = [[-1]*100 for _ in range(100)]

# 우하향
RD_D = [1, 1]
# 왼쪽
L_D = [0, -1]
# 위쪽
U_D = [-1, 0]
# 현재 방향
Now_D = RD_D

number = 0
count = N-1
x, y = 0, 0
board[x][y] = 0

while count > -1:
    small_count = 0
    while small_count < count:
        x, y = x + Now_D[0], y + Now_D[1]
        small_count += 1
        if number == 9:
            number = 0
        else:
            number += 1
        if board[x][y] == -1:
            board[x][y] = number

    if Now_D == RD_D:
        Now_D = L_D

    elif Now_D == L_D:
        Now_D = U_D

    elif Now_D == U_D:
        Now_D = RD_D

    x, y = x + Now_D[0], y + Now_D[1]
    if number == 9:
        number = 0
    else:
        number += 1

    if board[x][y] == -1:
        board[x][y] = number
    count -= 1

for i in range(len(board)):
    answer = ''
    for j in range(len(board)):
        if board[i][j] != -1:
            answer += str(board[i][j]) + ' '
    print(answer)

