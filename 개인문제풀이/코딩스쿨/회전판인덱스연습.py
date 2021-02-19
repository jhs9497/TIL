for tc in range(1, int(input())+1):
    N ,M, X, Y = map(int, input().split()) # N = 가로의 크기 M = 세로의 크기 X,Y 는 현재좌표
    X -= 1
    Y -= 1  # 코딩 인덱스 화
    X, Y = Y, X
    # board_map 구현
    board_map = [list(map(int, input().split())) for _ in range(M)]

    print(board_map[X][Y])