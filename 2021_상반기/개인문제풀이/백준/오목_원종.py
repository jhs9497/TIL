
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    omok = [input() for _ in range(N)]   # 오목 받고
    ans = 'NO'
    # 행 검색
    for i in range(N): # 행
        count = 0  # 행마다 초기화해야하므로 사이에 위치
        for j in range(N): # 열
            if omok[i][j] == 'o':
                count += 1  # 'o'를 만나면 count에 +1
            else:
                count = 0 # 초기화
        # 한 행이 끝나고
        if count >= 5: # 만약 count가 5를 넘으면
            ans = 'YES'


    # 열 검색
    for i in range(N):  # 열
        count = 0  # 행마다 초기화해야하므로 사이에 위치
        for j in range(N):  # 행
            if omok[j][i] == 'o':
                count += 1  # 'o'를 만나면 count에 +1
            else:
                count = 0  # 초기화
        # 한 행이 끝나고
        if count >= 5:  # 만약 count가 5를 넘으면
            ans = 'YES'


    # 대각 탐색 1번 - 우하향 대각선

    for i in range(N):  #예를 들어 N이 10, i 1
        count_A = 0
        count_B = 0
        for j in range(N-i): # j 0 1 2 3 4 5 6 7 8 9
            if omok[i+j][j] =='o':
                count_A += 1
            else:
                count_A = 0
        if count_A >= 5:
            ans = "YES"
            break

        for j in range(N-i): # j 0 1 2 3 4 5 6 7 8 9
            if omok[j][i+j] == 'o':
                count_B += 1
            else:
                count_B = 0

        if count_B >= 5:
            ans = "YES"
            break

    # 대각 탐색 1번 - 우상향 대각선

    for i in range(N):  # 2
        count_A = 0
        count_B = 0
        for j in range(N-i):  # 0 1 2 3 4 5 6 7
            if omok[][] == 'o':
                count_A += 1
            else:
                count_A = 0
        if count_A >= 5:
            ans = "YES"
            break

        for j in range(i, N):  # 0 1 2 3 4 5 6 7 8 9
            if omok[j][N] == 'o':
                count_B += 1
            else:
                count_B = 0

        if count_B >= 5:
            ans = "YES"
            break

    print('#{} {}'.format(tc, ans))