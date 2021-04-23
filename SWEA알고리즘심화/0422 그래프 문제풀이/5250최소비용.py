def BFS(x,y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    Q = []
    Q.append((x,y))
    info[x][y] = 0
    while Q:
        X, Y = Q.pop(0)
        for i in range(4):
            New_X = X + dx[i]
            New_Y = Y + dy[i] # 여기까지는 일반 BFS랑 똑같지만
            if 0 <= New_X < N and 0 <= New_Y < N:
                gap = board[New_X][New_Y] - board[X][Y]
                # 지금 밟은 위치 - 이전에 밟은 위치 : 높낮이 따라 +일수도, 0일수도, -일수도 있다.
                G = max(gap, 0)
                # 0이랑 비교해서 둘 중 큰 값을 취하면 항상 알맞은 G값을 얻을 수 있다
                if info[New_X][New_Y] > info[X][Y] + G + 1:
                    info[New_X][New_Y] = info[X][Y] + G + 1
                    Q.append((New_X, New_Y))
                    # visited를 사용하는 대신 지금 발을 디딘 곳의 축적된 비용이
                    # 내가 지금까지 밟아온 코스의 비용 + 지금 밟은 비용 한 것보다 큰 경우에만
                    # Q에 추가해서 새로 탐색하도록 한다.
                    # why? 지금 내가 밟아온 코스의 비용이 만약 더 크다면 이 코스는 최소비용을 위한 코스에
                    # 적합하지 않으니 버려도 된다.
                    # 과거 시점에 다른 코스로 탐색한 경우가 더 최소비용에 가까운 코스라는 것을 알 수 있음
                    # 그래서 info에 초기값을 다 1e9(무한대)로 맞춰둔것

for tc in range(1, int(input())+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    info = [[1e9]*N for _ in range(N)]
    # 1e9는 무한대, 정보를 쌓아갈 board랑 같은 크기의 2중 포문을 만든다
    BFS(0,0) # 왼쪽 위부터 BFS 함수 입장
    print('#{} {}'.format(tc, info[N-1][N-1])) # 가장 오른쪽 아래에 적혀있는 값 출력