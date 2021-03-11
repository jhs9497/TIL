def BFS(x):
    result = []
    visited = [False]*(N+1) # 방문췌크
    queue = [x] # 큐 만들고
    visited[x] = True # 방문체크하고

    while queue: # 큐에 뭐라도 있는 동안에
        now_point = queue.pop(0) # 현재 point는 큐의 맨 아래 아이

        for i in info[now_point]:
            if visited[i] == False: # 만약 방문한적 없다면
                result.append(i)  # result에 추가
                visited[i] = True  # 방문췌크
                queue.append(i) # 큐에 추가

    return len(result) # while문 다 끝나면 리턴

N = int(input()) # 컴퓨터의 수
M = int(input()) # 각 컴퓨터 간의 연결수
link_list = []
for i in range(M):
    yaya = list(map(int, input().split()))
    link_list.append(yaya)

info = [[] for _ in range(N+1)] # visted처럼 +1 해서 만들었고 X번째 컴퓨터랑 연결된 모든 컴퓨터를 표현

for i in range(len(link_list)): # 0
    info[link_list[i][0]].append(link_list[i][1])
    info[link_list[i][1]].append(link_list[i][0])

print(BFS(1))