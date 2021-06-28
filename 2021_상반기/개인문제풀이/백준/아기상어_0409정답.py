import copy

def find_eat(x, y):   # 먹이감을 찾는 함수 / 전체 먹이 리스트를 뽑긴 뽑지만 사실상 가장 가까운 먹잇감을 구하고 싶은거다

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
                if space[new_x][new_y] <= size and visited[new_x][new_y] == False:
                    if space[new_x][new_y] != 0 and space[new_x][new_y] < size:
                        eat_list.append((new_x, new_y))
                        visited[new_x][new_y] = True
                    else:
                        visited[new_x][new_y] = True
                        queue.append((new_x, new_y))



def count_d(shark_x, shark_y, fish_x, fish_y):  # 먹이감과의 거리(시간)을 구하는 함수

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
                    return answer

                if Space[x][y] > size: # 만약 만난 물고기가 아기상어보다 크다면
                    continue

                if Space[x][y] <= size : # 만약 만난 물고기가 아기상어보다 같거나 작다면
                    Space[x][y] = 10 + Space[shark_x][shark_y] # 방문처리 + 카운팅 하고
                    queue.append((x, y)) # 큐에 추가

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

        # 가장 가까운 먹이를 찾았으니 사냥하고 죽였다는 의미로 0으로 만들고
        space[fish_x][fish_y] = 0
        # 상어 위치를 죽인 먹이 위치로 옮겨주고
        shark_x, shark_y = fish_x, fish_y
        count += 1 # 사냥 횟수 count +1 해주고
        if count == size: # 만약 size만큼 잡아먹었으면
            size += 1 # 사이즈업
            count = 0 # 카운트 초기화
        sec += D # sec 변수에 가까운 먹이감 찾았을 때 거리 = 시간 이므로 D 추가해주기

print(sec)



# 3
# 9 2 2
# 2 2 3
# 1 3 1 반례에서 막힘