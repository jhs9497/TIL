import sys
sys.stdin = open("miro.txt", "r")

def DFS(x, y):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    stack = []
    stack.append((x,y))
    while stack:
        r, c = stack.pop()
        for i in range(4):
            new_r = r + dr[i]
            new_c = c + dc[i]
            if 0 <= new_r < 100 and 0 <= new_c < 100:
                if miro[new_r][new_c] == 1:
                    continue
                if miro[new_r][new_c] == 0:
                    miro[new_r][new_c] = 1
                    stack.append((new_r, new_c))
                if miro[new_r][new_c] == 3:
                    return 1
    return 0

for _ in range(10):
    tc = int(input())
    miro = [list(map(int, input())) for _ in range(100)]
    print('#{} {}'.format(tc, DFS(1, 1)))