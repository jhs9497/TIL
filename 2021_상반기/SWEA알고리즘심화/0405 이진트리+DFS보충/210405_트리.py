def tree(R):
    global answer
    R = int(R)
    if R > 0:
        tree(board[R][2])
        answer += board[R][1]
        tree(board[R][3])


for tc in range(1, 11):
    N = int(input())
    board = [['0', '0', '0', '0'] for _ in range(N+1)]
    for i in range(1, N+1):
        info = list(input().split())
        for j in range(len(info)):
            board[i][j] = info[j]
    answer = ''
    tree(board[1][0])
    print('#{} {}'.format(tc, answer))

