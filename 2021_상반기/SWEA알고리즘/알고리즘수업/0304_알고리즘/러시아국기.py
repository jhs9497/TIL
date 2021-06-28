# 조합 총 경우의 수 = N-2 ~ 1 까지 다 더하기 ex) N이 6이면 4+3+2+1
# [w, b, r] 이 wbr은 각 색들이 칠해지는 끝 행렬 표현
# 만약에  N = 6 일때 [2, 3, 5]이면 0,1,2행렬은 흰색 / 3 행렬은 파란색 / 4,5행렬은 빨간색
# 끝을 표현한거라서 빨간색은 항상 5!
# 각각의 범위는 w : 0~ {(N-1) -2} / b : 1 ~ {(n-1) -1} / r : only (n-1) why?  b가 정해지면 r는 자동이라

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())

    Russia = [list(input()) for _ in range(N)]  # 초기 국기

    color_range = [[],[],[N-1]]  # 빨간색만 미리 표시

    for i in range(0, ((N-1)-2)+1):
        color_range[0].append(i) # 흰색 범위 리스트로 표시

    for j in range(1, ((N-1)-1)+1):
        color_range[1].append(j)  # 파란색 범위 리스트로 표시

    case = []

    for i in range(len(color_range[0])):
        for j in range(len(color_range[1])):
            if color_range[0][i] < color_range[1][j]:
                I = color_range[0][i]
                J = color_range[1][j]
                case.append([I, J, N-1])
    # 여기까지 국기 범위 조합 완료
    answer = 99999999999999999999999
    for i in range(len(case)):
        # case[i][0] = W의 범위
        # case[i[[1] = B의 범위
        # case[i][2] = R의 범위
        white = case[i][0]
        blue = case[i][1]
        red = case[i][2]
        count = 0
        for j in range(white+1): # 조합에서 구한 흰색의 범위까지 행으로 돌면서
            for k in range(M): # 열은 고정
                if Russia[j][k] != 'W': # 만약 W가 아니면
                    count += 1  # count에 더하기 1

        # Blue는 white 다음부터~ Blue까지
        for j in range(white+1, blue+1): # 조합에서 구한 흰색의 범위까지 행으로 돌면서
            for k in range(M): # 열은 고정
                if Russia[j][k] != 'B': # 만약 B가 아니면
                    count += 1  # count에 더하기 1
        # Red는 Blue 다음부터~ 끝까지
        for j in range(blue+1, red+1): # 조합에서 구한 흰색의 범위까지 행으로 돌면서
            for k in range(M): # 열은 고정
                if Russia[j][k] != 'R': # 만약 R이 아니면
                    count += 1  # count에 더하기 1

        # 하나의 조합에 대한 탐색 끝나면
        if answer > count:
            answer = count # 최솟값 구하기

    print('#{} {}'.format(tc, answer))

