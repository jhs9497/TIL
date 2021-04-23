from collections import deque

def BFS(x,y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    Q = deque()
    Q.append((x,y))
    info[x][y] = board[x][y]
    while Q:
        X, Y = Q.popleft()
        for i in range(4):
            New_X = X + dx[i]
            New_Y = Y + dy[i]
            if 0 <= New_X < N and 0 <= New_Y < N: # 여기까지는 일반 BFS랑 똑같지만
                if info[New_X][New_Y] > board[New_X][New_Y] + info[X][Y]:
                    info[New_X][New_Y] = board[New_X][New_Y] + info[X][Y]
                    Q.append((New_X, New_Y))
                    # visited를 사용하는 대신 지금 발을 디딘 곳의 축적된 비용이
                    # 내가 지금까지 밟아온 코스의 비용 + 지금 밟은 비용 한 것보다 큰 경우에만 갱신하고
                    # Q에 추가해서 새로 탐색하도록 한다.
                    # why? 지금 내가 밟아온 코스의 비용이 만약 더 크다면 이 코스는 최소비용을 위한 코스에
                    # 적합하지 않으니 버려도 된다.
                    # 과거 시점에 다른 코스로 탐색한 경우가 더 최소비용에 가까운 코스라는 것을 알 수 있음
                    # 그래서 info에 초기값을 다 1e9(무한대)로 맞춰둔것
N = 1
tc = 0
while N != 0:
    N = int(input())
    if N == 0:
        break
    board = deque([list(map(int, input().split())) for _ in range(N)])
    info = deque([[1e9]*N for _ in range(N)])
    # 1e9는 무한대, 정보를 쌓아갈 board랑 같은 크기의 2중 포문을 만든다
    BFS(0,0) # 왼쪽 위부터 BFS 함수 입장
    tc += 1
    print('Problem {}: {}'.format(tc, info[N-1][N-1])) # 가장 오른쪽 아래에 적혀있는 값 출력