# 사방탐색을 해서 0인 경우 더 전진한다
# 전진하다가 더 이상 갈 수 없으면 visted에 append한다
# 사방탐색이 모두 끝났는데 goal에 도착하지 못했으면 visted의 -1 인덱스값에서 재출발한다.
#


def search(S, Goal):
    x = S[0]
    y = S[1]
    stack = [[x,y]]
    visted = []
    if miro[x][y] ==3:
        return 1

    while len(stack) > 0:
        new_x = x + dx[i]
        new_y = y + dy[i]
        for i in range(4):
            if miro[new_x][new_y] == 1:
                visted.append([new_x, new_y])
            elif miro[new_x][new_y] == 3:
                return 1
            





for tc in range(1, int(input())+1):
    N = int(input())
    miro = [list(map(int, input())) for _ in range(N)]  # 미로 인풋으로 받고

    dx = [-1, 1, 0, 0]  # 상 하 좌 우
    dy = [0, 0, -1, 1]

    S = () # 스타트 포인트
    Goal = 3 # 종료 포인트

    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                S = [i,j]