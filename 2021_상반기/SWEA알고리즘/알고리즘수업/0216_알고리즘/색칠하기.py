test_case = int(input())

for tc in range(test_case):
    # 우선 전체 판을 그리고
    board = [[0] * 10 for _ in range(10)]

    N = int(input())
    for n in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
       # 1,  2,  3,  3  이라 가정
        for r in range(r1, r2+1): # 1, 2, 3
            for c in range(c1, c2+1): # 2, 3
                board[r][c] += color # 본판에 color에 따라 색칠

    # 한 번의 턴이 끝나면 칠해진 보드 확인
    count = 0
    for i in range(10):
        for j in range(10):
            if board[i][j] == 3:
                count += 1

    print("#{} {}".format(tc+1, count))


