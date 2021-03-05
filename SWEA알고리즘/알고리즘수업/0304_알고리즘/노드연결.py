def search(S, G, visited):
    queue = []
    queue.append(S)  # 초기 스타트값 넣고 S G = 1, 6 이면 1!
    while queue: # queue가 뭐라도 있는 동안!
        x = queue.pop(0)
        for i in road[x]:
            if visited[i] == 0:
                visited[i] = visited[x] + 1
                queue.append(i)
    return visited[G]  # G인 6에 해당하는


for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    # V개의 노드
    # E개의 간선정보
    info = [[0]]+[list(map(int, input().split())) for _ in range(E)]
    # 입력 값으로 받은 간선정보 앞에 [0]을 넣어준 이유는 인덱스를 좀더 편하게 사용하고자 ?
    S, G = map(int, input().split())
    visited = [0] * (V + 1)  # 방문 체크 + count 표시

    road = [[] for _ in range(V+1)] # 1의 인덱스에는 1이 갈 수 있는 노드 / 2는 2가 갈 수 있는 / 3은 3이 갈 수 있는 노드 넣기 위함

    for i in range(1, len(info)):
        road[info[i][0]].append(info[i][1])  # 양방향
        road[info[i][1]].append(info[i][0])  # 추가
    # 내가 하고 싶은거
    #[[], [3, 4], [3, 5], [1, 2], [1, 6], [2], [4]]


    print('#{} {}'.format(tc, search(S, G, visited)))