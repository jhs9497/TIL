import sys
sys.stdin = open('사다리.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    X_list = [] # 시작점리스트를 구하고
    for x in range(100):
        if ladder[0][x] == 1:
            X_list += [x]

    for X in X_list: # X 시작점을 하나씩 꺼내면서 우선 첫번째 하나만 꺼내보자
        x = X # 첫번째 x는 0
        y = 0
        d = 0
        while y < 99 : # Y가 99미만일때 돌린다
            if x-1 >= 0 and ladder[y][x-1] == 1 and (d == 0 or d == 1):  # 만약 왼쪽값이 1이고 내가 온 방향이 위거나 왼쪽이면
                x = x-1
                d = 1

            elif x+1 < 100 and ladder[y][x+1] == 1 and (d == 0 or d == -1): # 오른쪽
                x = x+1
                d = -1

            else:
                y = y + 1
                d = 0

        if ladder[y][x] == 2:
            print("#{} {}".format(tc, X))







