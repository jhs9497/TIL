dx = [-1, 1, 0, 0]  # 상 하 좌 우
dy = [0, 0, -1, 1]

def dfs(row, col):
    ST = []
    visted = [[False] * N for _ in range(N)]
    ST.append((row, col)) #튜플로 묶어서
    visted[row][col] = True

    while len(ST) > 0:
        (row, col) = ST.pop(-1) # 튜플로 뽑아오기
        # 인접한 4방향에 대하여 반복처리
        for i in range(4):
            newR = row + dx[i]
            newC = col + dy[i]
            # 방문 여부
            # 방문 안했고 갈 수 있으면 스택에 append
            if 0 <= newR < N and 0 <= newC < N and not visted[newR][newC] and miro[newR][newC] != '1':
                if miro[newR][newC] == '3':
                    return 1
                ST.append((newR, newC))
                visted[newR][newC] = True

    return 0



for tc in range(1, int(input())+1):
    N = int(input())
    miro = [input() for _ in range(N)] # 미로 받고

    for i in range(N):
        if '2' in miro[i]: # 새로운 메소드
            col = miro[i].index('2')
            row = i
            break




    res = dfs(row, col)
    print('#{} {}'.format(tc, res))



