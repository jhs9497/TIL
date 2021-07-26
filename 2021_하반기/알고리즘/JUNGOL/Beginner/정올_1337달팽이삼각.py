def DFS(x, y):
    # 우하향
    RD_D = [1, 1]
    # 왼쪽
    L_D = [0, -1]
    # 위쪽
    U_D = [-1, 0]
    # 현재 방향
    Now_D = RD_D
    r, c = x, y
    stack = []
    stack.append((r, c))
    number = 0
    board[r][c] = number
    count = 0
    while stack and count < N**N:
        (r, c) = stack.pop()
        New_r, New_c = r + Now_D[0], c + Now_D[1]
        if 0 <= New_r < N and 0 <= New_c < N and board[New_r][New_c] == -1:
            number += 1
            board[New_r][New_c] = number
            stack.append((New_r, New_c))
            if number == 9:
                number = -1

        else:
            if Now_D == RD_D:
                Now_D = L_D
            elif Now_D == L_D:
                Now_D = U_D
            elif Now_D == U_D:
                Now_D = RD_D

            stack.append((r, c))
        count += 1


N = int(input())

board = [[-1]* N for _ in range(N)]

DFS(0, 0)

for i in range(len(board)):
    answer = ''
    for j in range(len(board)):
        if board[i][j] != -1:
            answer += str(board[i][j]) + ' '
    print(answer)
