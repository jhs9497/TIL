n, m = 5, 6
y, x = 2 ,1
arr = [[0,1,1,2,3],[2,5,-1,2,0],[10,29,17,-1,3],[5,4,7,9,12],[11,19,-1,12,4],[7,8,9,1,3]]
dy = [0,0,1,-1]
dx = [1,-1,0,0]
di = int(input())

for j in range(3):
    ny = y + dy[di]
    nx = x + dx[di]

    if nx < 0 or ny < 0 or nx >= n or ny >= m:
        break
    if arr[ny][nx] == -1:
        break
    y = ny
    x = nx
    print(arr[y][x])