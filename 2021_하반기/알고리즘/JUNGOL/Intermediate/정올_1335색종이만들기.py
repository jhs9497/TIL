N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

blue = 0
white = 0

def check(x, y, size):
    global board
    global blue
    global white
    flag = True
    now = board[x][y]
    for i in range(x, x+size):
        for j in range(y, y+size):
            if board[i][j] != now:
                flag = False
                break
        if flag == False:
            break

    if flag == True:
        if board[x][y] == 1:
            blue += 1
        else:
            white += 1
        return

    else:
        check(x,y,size//2)
        check(x+(size//2), y, size//2)
        check(x, y+(size//2), size//2)
        check(x+(size//2), y+(size//2), size//2)

check(0, 0, N)

print(white)
print(blue)
