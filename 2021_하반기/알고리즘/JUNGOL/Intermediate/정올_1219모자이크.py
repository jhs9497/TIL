N, M = map(int, input().split())
C_paper = int(input())
mistake = int(input())
board = [[0]*(M) for _ in range(N)]
max_X = 0
for _ in range(mistake):
    X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    board[X][Y] = 1
    if max_X <= X:
        max_X = X+1

def check(paper_size):
    global C_paper
    global M
    global board
    global max_X
    count = C_paper
    i = 0
    while i < M:
        is_mistake = False
        for j in range(max_X):
            if board[j][i] == 1:
                is_mistake = True
                break

        if is_mistake == True:
            i += paper_size
            count -= 1
            if count < 0:
                return check(paper_size+1)
        else:
            i += 1
    return paper_size

answer = check(max_X)
print(answer)



