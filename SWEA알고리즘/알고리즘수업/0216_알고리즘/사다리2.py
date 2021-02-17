import sys
sys.stdin = open('사다리.txt', 'r')

# 2가 보인다면 그 시작점이 답이다

for tc in range(1, 2):
    N = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]



    x = 3
    y = 0
    d = 0
    while y < 99 : # Y가 99미만일때 돌린다
        if ladder[y][x-1] == 1 and d == 0 or 1:  # 만약 왼쪽값이 1이고 내가 온 방향이 위거나 왼쪽이면
            x = x-1
            d = 1

        elif ladder[y][x+1] == 1 and d == 0 or -1: # 오른쪽
            x = x+1
            d = -1

        elif ladder[y+1][x] == 1:
            y = y + 1
            d = 0
