import copy

def check(x,y,k_x,k_y):
    check_screen = copy.deepcopy(screen)
    cancer_num = []
    for i in range(x, k_x+1):
        for j in range(y, k_y+1):
            check_screen[i][j] = -1  # 방사선으로 치료하고

    for i in range(P+2):
        for j in range(P+2):
            if check_screen[i][j] > 0: # 종양이 있으면
                cancer_num.append(check_screen[i][j]) # 추가
    count = len(set(cancer_num))

    if count <= M:
        return abs(x-k_x)+1
    else:
        return 99999999999999




for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    cancer = [list(map(int, input().split())) for _ in range(N)]
    # [좌하단좌표, 우상단좌표]로 통일시키자
    for i in range(len(cancer)):

        # [우상단좌표, 좌하단좌표]로 들어가있는 경우
        if cancer[i][0] - cancer[i][2] > 0 and cancer[i][1] - cancer[i][3] > 0:
            cancer[i][1], cancer[i][3] = cancer[i][3], cancer[i][1]
            cancer[i][0], cancer[i][2] = cancer[i][2], cancer[i][0]

        # [좌상단좌표, 우하단좌표]로 들어가있는 경우
        elif cancer[i][0] - cancer[i][2] < 0 and cancer[i][1] - cancer[i][3] > 0:
            cancer[i][1], cancer[i][3] = cancer[i][3], cancer[i][1]

        # [우하단좌표, 좌상단좌표]로 들어가있는 경우
        elif cancer[i][0] - cancer[i][2] > 0 and cancer[i][1] - cancer[i][3] < 0:
            cancer[i][0], cancer[i][2] = cancer[i][2], cancer[i][0]

        # 마지막으로 우상단좌표 x,y값 -1씩 해준다.
        cancer[i][2] -= 1
        cancer[i][3] -= 1

    P = max(max(cancer)) # 종양중 가장 우상단에 있는 좌표

    # 종양을 그릴 스크린은 여유있게 (P+2) * (P+2) 스크린으로 만든다
    screen = [[0]*(P+2) for _ in range(P+2)]


    # screen에 종양 그리기
    for i in range(len(cancer)):
        for j in range(cancer[i][0], cancer[i][2]+1):
            for k in range(cancer[i][1], cancer[i][3]+1):
                screen[j][k] = i+1 # 번호순으로 그려주기 겹치는건 생각 X

    # 여기까지 그림그리기 완료
    # 이제 K * K 정사각형으로 종양을 지워보기

    # K * K 방사선 치료 for문
    answer = 9999999999999999999999999
    for i in range(P+1):
        for j in range(P+1): # 사각형 방사선의 왼쪽위 기준지점
            for k in range(i, P+1):
                check_answer = check(i,j, i+k, j+k) # 함수에 넣기 K방사선의 좌하단점과 우상단점
                if answer > check_answer:
                    answer = check_answer

    print(answer)

