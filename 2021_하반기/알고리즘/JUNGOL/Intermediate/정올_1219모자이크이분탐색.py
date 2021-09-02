N, M = map(int, input().split())
C_paper = int(input())
mistake = int(input())
board = [0] * M
Max_X = 0
Max_Y = 0
for _ in range(mistake):
    X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    board[Y] = 1
    if Max_X <= X+1:
        Max_X = X+1
    if Max_Y <= Y+1:
        Max_Y = Y+1

left = min(Max_X, Max_Y)
right = max(Max_X, Max_Y)

while left <= right:
    count = C_paper
    paper_size = (left + right) // 2
    i = 0
    while i < M:
        if board[i] == 1:
            i += paper_size
            count -= 1
        else:
            i += 1

    if count >= 0:
        right = paper_size - 1
    else:
        left = paper_size + 1

print(left)


