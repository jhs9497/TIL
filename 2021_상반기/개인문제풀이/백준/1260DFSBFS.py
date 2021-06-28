def DFS(start_point):
    global info
    for i in range(len(info)):
        info[i].reverse()  # DFS에서는 처음 들어오는게 나중에 나가므로 info의 각 리스트들을 reverse해준다
        # info = [[], [4, 3, 2], [4, 1], [4, 1], [3, 2, 1]]
    result = []
    visited = [False]*(N+1)
    stack = [start_point] # 스택에 우선 넣어주고
    while stack: # 스택에 뭐라도 있는 동안 진행
        now_point = stack.pop() # 현재 지점은 stack 맨 위에 있는 포인트
        if visited[now_point] == False: # 만약 방문 전이라면
            result.append(now_point) # 최종결과에 추가
            visited[now_point] = True # 방문 처리

        for i in info[now_point]: # now_point기준 연결된 노드리스트를 돌면서
            if visited[i] == False:  # 만약 방문 전이라면
                stack.append(i)  # 스택에 다 추가

    return result # while문 다 끝나고 return


def BFS(start_point):
    global info
    for i in range(len(info)):
        info[i].reverse() # 위에서 reverse되어서 한번더 reverse...
        # info = [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]]
    result = []
    visited = [False]*(N+1)
    queue = [start_point] # 스택에 우선 넣어주고
    while queue: # 스택에 뭐라도 있는 동안 진행
        now_point = queue.pop(0) # 현재 지점은 queue 맨 아래에 있는 포인트
        if visited[now_point] == False: # 만약 방문 전이라면
            result.append(now_point) # 최종결과에 추가
            visited[now_point] = True # 방문 처리

        for i in info[now_point]: # now_point기준 연결된 노드리스트를 돌면서
            if visited[i] == False:  # 만약 방문 전이라면
                queue.append(i) # 연결된 노드들 스택에 추가

    return result # while문 다 끝나고 return

N, M, K = map(int, input().split())

N_list = [] # 처음 인풋 받은 리스트
for i in range(M):
    yaya = list(map(int, input().split()))
    N_list.append(yaya)

info = [[] for _ in range(N+1)] # visted처럼 +1 해서 만들었고 X번째 노드가 갈 수 있는 모든 노드를 표현

for i in range(len(N_list)): # 0
    info[N_list[i][0]].append(N_list[i][1])
    info[N_list[i][1]].append(N_list[i][0])

for i in range(len(info)):
    info[i].sort()
    # info = [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]]

DFS_K = DFS(K)
print(*DFS_K)
BFS_K = BFS(K)
print(*BFS_K)