for tc in range(1, int(input())+1):
    N = int(input())
    cell = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != 0 and i != N-1 and j != 0 and j != N-1 and cell[i][j] ==1:
                check = []
                # 위로 체크하기
                up = i
                up_cnt = 0
                while up > 0:
                    up_cnt += 1
                    up = up-1
                    if cell[up][j] !=0:
                        up = -1
                if up == 0:
                    check.append([up_cnt, up, j])

                # 아래로 체크하기
                down = i
                down_cnt = 0
                while down < N-1:
                    down_cnt += 1
                    down = down + 1
                    if cell[down][j] != 0:
                        down = N # while문 끝내기
                if down == N-1:
                    check.append([down_cnt, down, j])

                # 왼쪽으로 체크하기
                left = j
                left_cnt = 0
                while left > 0:
                    left_cnt += 1
                    left = left -1
                    if cell[i][left] != 0:
                        left = -1
                if left == 0:
                    check.append([left_cnt, i, left])

                # 오른쪽으로 체크하기
                right = j
                right_cnt = 0
                while right < N-1:
                    right_cnt += 1
                    right = right + 1
                    if cell[i][right] != 0:
                        right = N
                if right == N-1:
                    check.append([right_cnt, i, right])

                print(check)





























                # check.sort() # cnt가 낮은순부터 정렬하고
                # if check:
                #     answer += check[0][0]
                #
                # # core인 i,j와 목표가 된 check[0][1], check[0][2]사이를 전선으로 표시해줘야함
                # if check:
                #     power_i, power_j = check[0][1], check[0][2]
                #     if i == power_i: # 만약 전선이 수평으로 놓인 경우
                #         if j > power_j:
                #             for x in range(power_j, j):
                #                 cell[i][x] = 2
                #         else:
                #             for x in range(j+1, power_j+1):
                #                 cell[i][x] = 2
                #
                #     if j == power_j: # 만약 전선이 수직으로 놓인 경우
                #         if i > power_i:
                #             for x in range(power_i, i):
                #                 cell[x][j] = 2
                #         else:
                #             for x in range(i+1, power_i+1):
                #                 cell[x][j] = 2