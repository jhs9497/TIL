import copy

def count_d(shark_x, shark_y, fish_x, fish_y):
    visited = [[False]*N for _ in range(N)]
    visited[shark_x][shark_y] = True
    queue = []
    queue.append((shark_x, shark_y))
    sec = 0  # 초재기
    while queue:
        shark_x, shark_y = queue.pop(0)
        for i in range(4):
            x = shark_x + dx[i]
            y = shark_y + dy[i]

            if 0 <= x < N and 0 <= y < N:
                if (x, y) == (fish_x, fish_y) and visited[x][y] == False: # 만약 타겟한 fish의 인덱스와 같으면
                    sec += 1
                    return sec

                if space[x][y] > size: # 만약 만난 물고기가 아기상어보다 크다면
                    continue

                if space[x][y] <= size and visited[x][y] == False: # 만약 만난 물고기가 아기상어보다 같거나 작다면
                    visited[x][y] = True # 방문처리
                    sec += 1 #
                    queue.append((x, y)) # 큐에 추가

######################################################################################

def hunt(shark_x, shark_y, fish_x, fish_y):
    visited = [[False]*N for _ in range(N)]
    visited[shark_x][shark_y] = True
    queue = []
    queue.append((shark_x, shark_y))
    sec = 0  # 초재기
    while queue:
        shark_x, shark_y = queue.pop(0)
        for i in range(4):
            x = shark_x + dx[i]
            y = shark_y + dy[i]

            if 0 <= x < N and 0 <= y < N:
                if (x, y) == (fish_x, fish_y) and visited[x][y] == False: # 만약 타겟한 fish의 인덱스와 같으면
                    sec += 1
                    return sec

                if space[x][y] > size: # 만약 만난 물고기가 아기상어보다 크다면
                    continue

                if space[x][y] <= size and visited[x][y] == False: # 만약 만난 물고기가 아기상어보다 같거나 작다면
                    visited[x][y] = True # 방문처리
                    sec += 1 #
                    queue.append((x, y)) # 큐에 추가


#########################################################################################

def find_eat(x, y):

    visited = [[False]*N for _ in range(N)]
    visited[x][y] = True
    queue = []
    queue.append((x, y))
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < N and 0 <= new_y < N:
                if (space[new_x][new_y] == 0 or space[new_x][new_y] == size) and visited[new_x][new_y] == False:
                    # 만약 space에서 아무것도 없는 길이거나 나랑 같은 크기 즉 지나가기만 해야하면서 방문한적 없다면 방문체크 + 큐에 추가
                    visited[new_x][new_y] = True
                    queue.append((new_x, new_y))

                if 0 < space[new_x][new_y] < size and visited[new_x][new_y] == False:
                    # 내 사냥감이면서 방문한적 없다면 방문체크 + 큐에 추가 + 사냥감리스트에 추가
                    visited[new_x][new_y] = True
                    queue.append((new_x, new_y))
                    eat_list.append((new_x, new_y))



N = int(input())

space = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            shark_x, shark_y = i, j # 아기 상어 위치
            space[i][j] = 0 # 아기상어 위치 0으로 바꿔주기 why? 9라는 숫자가 움직임에 제약을 줌

size = 2 # 물고기 초기 사이즈
sec = 0 # 총 시간 재는 초시계
count = 0 # 물고기 2마리 먹으면 size가 +1 되어야한다
door = 'open'  # 더 이상 먹을만한 물고기가 없을 때 이 door를 'close'로 바꾸고 while문 빠져나오기

while door == 'open':
    eat_list = [] # 먹이 리스트
    find_eat(shark_x, shark_y) # 먹이 찾으러 고고
    if len(eat_list) == 0: # 만약 eat_list가 비어있으면
        door = 'close'
    else:

        # 가장 가까운 먹이 찾기
        eat_list.sort()
        # 왼쪽 위에서 오른쪽 아래로 향하게 sort 해주고
        D = 999999
        fish_x, fish_y = 0, 0
        for i in range(len(eat_list)-1, -1, -1):
         # 동일거리면 왼쪽 위에 놈을 먹어야 하므로 리스트 거꾸로 돌리면서 먹잇값이랑 나 사이의 거리 구하기
            d = count_d(shark_x, shark_y, eat_list[i][0], eat_list[i][1])
            if D >= d:
                D = d
                fish_x, fish_y = eat_list[i][0], eat_list[i][1]

        # 가장 가까운 먹이를 찾았으니 사냥 함수에 넣어 사냥하고
        sec_ = hunt(shark_x, shark_y, fish_x, fish_y)
        # 가장 가까운 먹이 죽였다는 의미로 0으로 만들고
        space[fish_x][fish_y] = 0
        # 상어 위치 죽인 먹이 위치로 옮겨주고
        shark_x, shark_y = fish_x, fish_y
        count += 1 # count +1 해주고
        if count == size: # 만약 size만큼 잡아먹었으면
            size += 1 # 사이즈업
            count = 0 # 카운트 초기화
        sec += sec_ # sec 변수에 사냥 함수값 추가해주기



print(sec)