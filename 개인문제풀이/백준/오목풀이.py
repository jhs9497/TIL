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


    # 대각 탐색 1번 - 우하향 대각선에서 아랫부분
    # 쌍대각 X를 기준으로 총 4개로 쪼개서 대각을 탐색했음

    for i in range(N):
        j_list = []
        k_list = []
        for j in range(i, N): # i에 따라서 0~N / 1~N / 2~N로 나아감  -> 행
            j_list.append(j)  # 인덱스 리스트에 추가
        for k in range(0, N-i): # 열 i에 따라서 0~N / 0~N-1 / 0~N-2 로 나아감 -> 열
            k_list.append(k)  # 인덱스 리스트에 추가

        # 여기까지 i기준 대각선 하나 만듬
        # 대각선 탐색
        count = 0
        for a in range(len(j_list)):  # len(k_list)해도 상관은 없음
            if omok[j_list[a]][k_list[a]] == 'o':
                count += 1
            else:
                count = 0

        if count >= 5:
            ans = 'YES'


    # 대각 탐색 2번 - 우하향 대각선 기준 윗부분
    for i in range(N):
        j_list = []
        k_list = []
        for j in range(0, N -i):
            j_list.append(j)
        for k in range(i, N):
            k_list.append(k)

        count = 0
        for a in range(len(j_list)):
            if omok[j_list[a]][k_list[a]] == 'o':
                count += 1
            else:
                count = 0

        if count >= 5:
            ans = 'YES'



    # 대각 탐색 3번 - 우상향 대각선 기준 윗부분 N =10
    for i in range(N-1, -1, -1):
        j_list = []
        k_list = []
        for j in range(i, -1, -1):
            j_list.append(j)
        for k in range(i+1):
            k_list.append(k)

        count = 0
        for a in range(len(j_list)):
            if omok[j_list[a]][k_list[a]] == 'o':
                count += 1
            else:
                count = 0

        if count >= 5:
            ans = 'YES'


    # 대각 탐색 4번 - 우상향 대각선 기준 아랫부분
    for i in range(N-1, -1, -1):
        j_list = []
        k_list = []
        for j in range(N-1, N-i-2, -1):
            j_list.append(j)
        for k in range(N-i-1, N):
            k_list.append(k)

        count = 0
        for a in range(len(j_list)):
            if omok[j_list[a]][k_list[a]] == 'o':
                count += 1
            else:
                count = 0

        if count >= 5:
            ans = 'YES'

    print('#{} {}'.format(tc, ans))