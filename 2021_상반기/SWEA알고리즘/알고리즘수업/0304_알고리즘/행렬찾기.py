for tc in range(1, int(input())+1):
    N = int(input())
    cordi = [list(map(int, input().split())) for _ in range(N)]
    select = [] # 행렬 크기, 행, 렬 저장

    for i in range(N):
        for j in range(N):
            if cordi[i][j] > 0: # 만약 화학물질을 처음으로 마주한다면
                cordi[i][j] = -1 # -1을 넣어서 체크해주고
                dx = 1 # 우측으로 쭉쭉
                dy = 1 # 아래로 쭉쭉
                r, c = i, j
                R_d = 1 # 초기값 1
                C_d = 1
                while 0 <= r < N and 0 <= c+dy < N and cordi[r][c+dy] != 0 : # 오른쪽으로 가면서 0을 마주치기 전까지 / r 고정

                    R_d += 1 # 갔으니깐 추가
                    cordi[r][c+dy] = -1 # 체크
                    c = c+dy # 한칸 더 간다

                # 높이도 체크

                while 0 <= r+dx < N and 0 <= c < N and cordi[r+dx][c] != 0 : # c 고정
                    C_d  += 1
                    cordi[r+dx][c] = -1 # 체크
                    r = r + dx

                # # 왼쪽 위 모서리 = [i, j] // 오른쪽 아래 모서리 = [c, r] -> 다 -1로 바꿔줘야 나중에 혼란 안일어남
                for a in range(i, r+1):
                    for b in range(j, c+1):
                        cordi[a][b] = -1

                # 하나의 사각형 탐색이 끝나면
                s = R_d * C_d  # 사이즈 계산해서 넣어주고
                if [s, C_d, R_d] not in select: # 만약 중복되는게 없다면
                    select.append([s, C_d, R_d])

    select.sort()  # 2차원까지 정렬

    count = len(select) # 답 맨 앞에는 사각형 갯수

    answer = []

    for i in range(len(select)):
        answer.append(select[i][1]) # 행
        answer.append(select[i][2])

    print('#{} {}'.format(tc, count), end=" ")
    print(*answer)




