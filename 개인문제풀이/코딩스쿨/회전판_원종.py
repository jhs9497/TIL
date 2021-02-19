n, m, x, y = 5, 6, 1, 2  # x,y 의 값은 열과 행
arr = [[0, 1, 1, 2, 3], [2, 5, -1, 2, 0], [10, 29, 17, -1, 3], [5, 4, 7, 9, 12], [11, 19, -1, 12, 4], [7, 8, 9, 1, 3]]
K = 3
To = [2, 4, 1]
L = 3
k = 0  # To의 위치값
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
cnt = 0
for i in range(2):

    di, d, r = map(int, input().split())
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

    for j in range(2):  # To의 값 만큼 움직이겠다.

        ny = y + dy[di]
        nx = x + dx[di]

        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            break
        if arr[ny][nx] == -1:
            break
        y = ny
        x = nx

        cnt += arr[y][x]
        arr[ny][nx] = 0

        print(arr[ny][nx])

