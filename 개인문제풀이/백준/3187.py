def BFS(x, y):
    num_v = 0
    num_k = 0
    if New_Yard[x][y] == 1: # 만약 함수호출된 아이가 늑대면
        num_v +=1 # 늑대 +1로 시작
    else: # 양이면
        num_k += 1 # 양 +1로 시작
    New_Yard[x][y] = 0 # 나 자신 빈공간으로 초기화
    queue = [(x,y)]
    while queue:
        r,c = queue.pop(0)
        for i in range(4):
            nx = r + dx[i]
            ny = c + dy[i]

            if 0<=nx<N and 0<=ny<M:
                if New_Yard[nx][ny] == 3:
                    continue # 울타리면 넘어가고
                if New_Yard[nx][ny] == 0:
                    New_Yard[nx][ny] = 3  # 울타리로 초기화
                    queue.append((nx, ny))  # 빈공간이면 방문체크
                if New_Yard[nx][ny] == 1:  # 늑대일때
                    num_v += 1  # 늑대숫자에 추가
                    New_Yard[nx][ny] = 3  # 울타리로 초기화
                    queue.append((nx,ny))  # 방문체크
                if New_Yard[nx][ny] == 2:
                    num_k += 1  # 양숫자에 추가
                    New_Yard[nx][ny] = 3  # 울타리로 초기화
                    queue.append((nx, ny))  # 방문체크

    if num_v >= num_k: # while문 다 종료된 후 만약 늑대수가 같거나 더 많다면
        num_k = 0  #양의 수는 0으로
    else: # 반대면
        num_v = 0 #늑대수 0으로

    return num_v, num_k  # 둘다 리턴

N, M = map(int, input().split())

Yard = [input() for _ in range(N)]

New_Yard = [[0]*M for _ in range(N)]

# 스트링이기 때문에 변경 불가능해서 int화
for i in range(N):
    for j in range(M):
        if Yard[i][j] =='v':
            New_Yard[i][j] = 1
        if Yard[i][j] =='k':
            New_Yard[i][j] = 2
        if Yard[i][j] =='#':
            New_Yard[i][j] =3
# 1 -> 늑대
# 2 -> 양
# 3 -> 울타리

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

total_v = 0  # 최종 늑대의 수
total_k = 0  # 최종 양의 수

for i in range(N):
    for j in range(M):
        if New_Yard[i][j] == 1 or New_Yard[i][j] == 2:
            (v, k) = (BFS(i, j))
            total_v += v  # 최종 늑대의 수 + 함수돌리면서 얻은 늑대수
            total_k += k  # 최종 양의 수 + 함수돌리면서 얻은 양의 수

print(total_k, total_v)