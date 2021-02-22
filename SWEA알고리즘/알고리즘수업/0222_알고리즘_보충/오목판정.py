import sys
sys.stdin = open("오목.txt")


# 델타를 이용해서 해보자
def check(x, y):
    for i in range(8):
        cnt = 1 # 돌을 이미 하나 셌으므로
        r, c = x+dx[i], y+dy[i]
        while 0 <= r < N and 0 <= c < N and board[r][c] == 'o':
            cnt += 1
            r, c = r+dx[i], c+dy[i]
        if cnt > 4: return True
    return False

ans = ["NO", "YES"]
dx = [-1, 1, 0, 0, -1, 1, 1, -1]
dy = [0, 0, -1, 1, 1, 1, -1, -1]
for tc in range(1, int(input())+1):
    N = int(input())
    board = [list(input()) for _ in range(N)]

    flag = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == '.': continue
            if check(i, j): # check가 참이면
                flag = 1
                break
        if flag: break # flag가 참이면

    print("#{} {}".format(tc, ans[flag]))