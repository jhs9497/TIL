for tc in range(1, int(input())+1):
    N = int(input())  # 행렬의 수
    arr = [[[0]*N for _ in range(N)] for _ in range(4)] # 면 4개 만든겨

    for i in range(N):
        arr[0][i] = list(map(int, input().split()))  # 0번째 면에 초기 행렬 저장

    # 회전
    for k in range(1, 4):
        for i in range(N):
            for j in range(N):
                arr[k][j][N-1-i] = arr[k-1][i][j]

    print('#{}'.format(tc))
    for i in range(N):
        for k in range(1,4):
            if k != 1: print(end=" ")
            for j in range(N):
                print(arr[k][i][j], end = "")
        print()