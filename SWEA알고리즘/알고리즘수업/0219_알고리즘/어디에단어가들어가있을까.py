# import sys
# sys.stdin = open("퍼즐.txt")
for tc in range(1, int(input())+1):
    N, M= map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    answer = 0
    for i in range(N):
        # 가로탐색
        count = 0
        for j in range(N):
            if puzzle[i][j] == 1:
                count += 1

            if puzzle[i][j] == 0:
                if count == M:
                    answer += 1
                    count = 0
                else:
                    count = 0
        if count == M:
            answer += 1

       # 세로 탐색
        count = 0
        for j in range(N):
            if puzzle[j][i] == 1:
                count += 1

            if puzzle[j][i] == 0:
                if count == M:
                    answer += 1
                    count = 0
                else:
                    count = 0
        if count == M:
            answer += 1

    print('#{} {}'.format(tc, answer))






