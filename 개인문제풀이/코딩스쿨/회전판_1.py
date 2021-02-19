for tc in range(1, int(input())+1):
    N ,M, X, Y = map(int, input().split()) # N = 가로의 크기 M = 세로의 크기 X,Y 는 현재좌표
    X -= 1
    Y -= 1  # 코딩 인덱스 화
    X, Y = Y, X  #코딩 인덱스 화 2
    # board_map 구현
    board_map = [list(map(int, input().split())) for _ in range(M)]
    K = int(input()) # 회전판 칸의 개수
    circle = list(map(int, input().split())) # 회전판 구성숫자  # 1 (시계방향) 이면 역방향 / 2 (반시계방향) 이면 정방향
    L = int(input()) # 이동시키는 횟수
    k = 0
    point = 0  # 점수담을 변수 맨 바깥에 있어야 함

    for l in range(L):
        # 여기까지 입력완료
        # 구해야 할 것 : 1) 점수의 합, 2) 마지막 좌표
        # 유의 사항 : -1을 만나거나 보드 바깥으로 나가면 그 전 좌표에서 멈추기
        di, d, r = input().split()  # 우선 스트링으로 받고 나중에 숫자는 int로 사용하기
        r = int(r)
        d = int(d)
        if r > K:
            while r > K:
                r -= K
        if d == 2:
            if 0 <= k + r < K:
                k = k + r
            else:
                k = k + r - K
        if d == 1:
            if 0 < k - r < K:
                k = k - r
            else:
                k = k - r + K

        r = circle[k]
        up_down = [0, 0, 1, -1, 0]
        right_left = [1, -1, 0, 0, 0]   # 움직임을 나타낼 변수
        d = 4  # 방향 E , W,  N,  S  에 맞춰서 0,1,2,3   4 ( 처음 위치에서 쓸 0,0 인덱스 )
        # point = 0  # 점수담을 변수 맨 바깥에 있어야 함

        while r >= 0: # r이 가야하는 정도이니 이 r값이 -1이 되면 움직임을 멈출거임 원랜 0이 맞으나 처음 위치한 point도 가져와야 하므로
            # 시작 좌표는 X, Y로 정해졌음
            if X + up_down[d] < 0 or X + up_down[d] >= M or Y + right_left[d] < 0 or Y + right_left[d] >= N:
                r = -1    # 만약 좌표가 범위를 넘어가 버리면 r을 -1 로 하고 while문 끝내기
                break

            if board_map[X + up_down[d]][Y + right_left[d]] == -1:
                r = -1    # -1을 만나도 마찬가지
                break

            point += board_map[X+up_down[d]][Y+right_left[d]]
            board_map[X+up_down[d]][Y+right_left[d]] = 0 # 지나간 자리는 0으로
            # 현재 초기값 d = 4 이기 때문에 up_down[d]와 right_left[d] 모두 0으로 초기값인
            # board_map[X][Y]로 표현 가능
            if di == 'E':    # order로 받은 방향에 따라 d 값을 변환해줌
                d = 0
            if di == 'W':
                d = 1
            if di == 'S':
                d = 2
            if di == 'N':
                d = 3
            r -= 1 # r값 -1 해주기
            X = X+up_down[d]
            Y = Y+right_left[d]   # X,Y 좌표도 뽑아줘야 하므로 기록해주기

            print(board_map[X][Y])

        # while 문 다 끝나면 쌓여 있는 point 와 X, Y 좌표 뽑아주기

    # print('#{} {} {} {}'.format(tc, point, X, Y))

