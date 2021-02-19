# 방향을 정해놓고 더 이상 4방향에 갈 공간이 없을때까지

# 오른쪽 -> 아래 -> 왼쪽 -> 위 순서

for tc in range(1, int(input())+1):
    N = int(input())

    # 우선 0으로 이루어진 2차원 배열을 만들자

    snail = [[0]*N for _ in range(N)]

    x, y = 0, 0 # 달팽이의 스타트 점은 왼쪽 맨 위
    number = 1 # 달팽이가 지나가며 적을 숫자
    d = 0 # 마지막 else인 경우에 while문 빠져나오게 하는 용도 + 방향 설정
    while d < 4 : # 갈 곳이 없을때까지
        # 오른쪽 먼저 확인
        if x+1 < N and snail[x+1][y] == 0: #and d == 0: d == 3:  # 달팽이 오른쪽에 0이라는 공간이 있다면
            snail[x][y] = number # 지금 서있는 자리에 number 박고
            x = x+1 # x 한칸 움직여주고
            number += 1 # number도 하나 증가
            d = 0

        # 오른쪽에 0이 없다면 아래 확인
        elif y+1 < N and snail[x][y+1] == 0: #and d == 1 d == 0:
            snail[x][y] = number
            y = y+1
            number += 1
            d = 1

        # 아래에도 0이 없다면 왼쪽 확인
        elif x-1 >= 0 and snail[x-1][y] == 0: #and d == 2 d == 1:
            snail[x][y] = number
            x = x-1
            number += 1
            d = 2

        # 왼쪽에도 0이 없다면 위쪽 확인
        elif y-1 >= 0 and snail[x][y-1] == 0: #and d ==3: #d == 2:
            snail[x][y] = number
            y = y-1
            number += 1
            d = 3

        # 어느쪽에도 0이 없다면
        else:
            snail[x][y] = number
            d = 1 # while문 나오기

    print('#{}'.format(tc))

    for i in range(len(snail)):
        snail_answer = ''
        for j in range(len(snail)):
            snail_answer += str(snail[j][i])
            snail_answer += ' '
        print(snail_answer)



