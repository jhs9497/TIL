def search(x, y):
    answer = 0 # 답이 될 친구
    miro[x][y] = 0 # 출발점 걍 0으로 넣어주고
    stack = []  # 스택 만들고
    stack.append((x,y)) # 스택에 (x,y) 추가
    while stack: # 스택에 뭐라도 있는 동안에
        x,y = stack.pop()  # 스택에 맨 위 인덱스 빼서 그 스택이 기준
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]  # 4방향 탐색하면서
            if nx >= 0 and nx < N and ny >= 0 and ny < N: # 범위 안에 있으면서
                if miro[nx][ny] == 1: # 막혀있으면
                    continue # 넘어가고
                if miro[nx][ny] == 'goal' : # 골 지점을 만나면
                    miro[nx][ny] = -1 # -1로 표시하고
                    answer = miro[x][y] # 이전 인덱스로 answer 값넣고
                    break # 그만!
                if miro[nx][ny] ==0: # 뚫려있으면
                    miro[nx][ny] = miro[x][y] +1 # 방문한 곳 벽으로 만들어주면서 +1 해주기
                    stack.append((nx, ny)) #  스택에 추가
    if miro[c][d] == 'goal' : # 만약 goal지점이 그대로 'goal'이면
        return 0 # 0을 리턴하고
    else:
        return answer  # -1로 도착되어있다면 answer 리턴



for tc in range(1, int(input())+1):
    N = int(input())
    miro = [list(map(int, input())) for _ in range(N)]

    st = () # 스타트포인트
    goal = () # 목표
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 3:
                st = (i, j)
            if miro[i][j] == 2:
                goal = (i, j)

    # 상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    a, b = st
    c, d = goal
    miro[c][d] = 'goal'  # goal 지점을 'goal'로 표현해주기

    print('#{} {}'.format(tc, search(a, b)))

