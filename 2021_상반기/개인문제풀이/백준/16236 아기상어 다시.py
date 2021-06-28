# 1. 아기상어 위치에서 가장 가까운 먹을 수 있는 물고리를 찾는다.
# 2. BFS 함수를 만들어서 그 물고기를 먹으러 가는 최소시간을 구한다.
# 3. 더 이상 먹을 수 있는 물고기가 없을 때까지 while문을 돌린다.

import copy
#################################################################################################
# 먹이와의 거리 구하는 함수

def fish_bfs(shark_x, shark_y, a, b):
    sample = copy.deepcopy(space)  # 이 함수 내부에서만 돌릴 Space 만들어주고
    visited = [[False] * N for _ in range(N)]
    queue = [(shark_x, shark_y)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    sample[shark_x][shark_y] = 0 # 나자신 0으로 초기화
    visited[shark_x][shark_y] = True # 방문처리
    while queue:
        shark_x, shark_y = queue.pop(0)
        for i in range(4):
            x = shark_x + dx[i]
            y = shark_y + dy[i]
            if 0 <= x < N and 0 <= y < N:
                if sample[x][y] <= size and visited[x][y] == False:
                    sample[x][y] = sample[shark_x][shark_y] + 1
                    visited[x][y] = True
                    queue.append((x,y))
                if (x, y) == (a, b):
                    return sample[a][b] # 먹잇감 만나면 return


    return -1 # 먹잇감이 있긴 하지만 큰 물고기들 사이에 쌓여있어서 접근할 수 없는 경우


##################################################################################################
# 먹이 먹어가며 아기상어가 sizeup 해가는 함수

def BFS(shark_x, shark_y, fish_x, fish_y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = []
    queue.append((shark_x, shark_y))
    Space = copy.deepcopy(space)  # 이 함수 내부에서만 돌릴 Space 만들어주고
    Space[shark_x][shark_y] = 10  # 카운팅을 위해 1 대신 10으로
    while queue:
        shark_x, shark_y = queue.pop(0)
        for i in range(4):
            x = shark_x + dx[i]
            y = shark_y + dy[i]

            if 0 <= x < N and 0 <= y < N:
                if (x, y) == (fish_x, fish_y): # 만약 타겟한 fish의 인덱스와 같으면
                    Space[x][y] = 10 + Space[shark_x][shark_y]
                    answer = Space[x][y] // 10 -1 # 10단위로 표현 카운팅을 1부터 시작했으니 1빼주기
                    space[x][y] = 0 # 본판 space에도 먹었다는 의미로 0으로 바꿔준다
                    return answer

                if Space[x][y] > size: # 만약 만난 물고기가 아기상어보다 크다면
                    continue

                if Space[x][y] <= size : # 만약 만난 물고기가 아기상어보다 같거나 작다면
                    Space[x][y] = 10 + Space[shark_x][shark_y] # 방문처리 하고
                    queue.append((x, y)) # 큐에 추가


##################################################################################################
# 초기 인풋값 + 핵심 whlie문

N = int(input())

space = [list(map(int, input().split())) for _ in range(N)]


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

    fish = [] # 먹을 수 있는 물고기 리스트 뽑기
    for i in range(N):
        for j in range(N):
            if space[i][j] < size and space[i][j] != 0: # 0이 아니면서 아기상어보다 작은 물고기 찾기
                fish.append(space[i][j])

    if fish == []: # 만약 공간에서 나보다 작은 물고기가 없다면
        door = 'close' # door를 닫고
        break

    else:
        # 물고기 인덱스 튜플형태로 리스트만들기
        fish_idx = []
        for i in range(N):
            for j in range(N):
                if space[i][j] in fish: # 만약 먹을 수 있는 물고기에 해당하면
                    # 현재 아기상어와의 거리도 함수로 구해서 물고기 리스트에 추가
                    d = fish_bfs(shark_x, shark_y, i, j)
                    if d == -1: # 만약 먹잇감이 있는데 못 먹는경우 넘어가고
                        continue
                    else:
                        fish_idx.append((d, i, j))
        if len(fish_idx) == 0: # 먹잇감할만한 친구가 1마리도 없다면
            door = 'close' # 문닫기
            break

        if door == 'open': # 먹잇감 체크 후에 여전히 door가 열려있으면
            # 만들어진 fish_idx를 sort를 통해 정렬하면서 fish_idx에 맨 앞 자리가 타겟물고기다
            fish_idx.sort()

            fish_x, fish_y = fish_idx[0][1], fish_idx[0][2]

            # 여기까지 아기상어의 위치랑 / 타겟 물고기의 위치를 찾았다.

            # BFS 함수만들어서 돌리기
            sec_ = BFS(shark_x, shark_y, fish_x, fish_y)
            # 물고기를 잡아 먹었으면
            shark_x, shark_y = fish_x, fish_y # 내 위치는 먹은 물고기 위치
            count += 1 # count +1 해주고
            if count == size: # 만약 size만큼 잡아먹었으면
                size += 1 # 사이즈업
                count = 0 # 카운트 초기화
            sec += sec_ # sec 변수에 추가해주기

print(sec) # 모든 while문 끝나고 축적된 sec 프린트


# 3
# 9 2 2
# 2 2 3
# 1 3 1 반례에서 막힘