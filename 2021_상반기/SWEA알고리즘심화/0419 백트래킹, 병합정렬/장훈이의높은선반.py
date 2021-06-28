def dfs(index, now):
    global min_
    if index == N: # 만약 index가 N이랑 똑같아지면 -> 1개의 부분집합에 대한 탐색이 끝났으면
        if now >= H: # 만약 처음에 인풋받은 높이보다 높고
            if now <= min_: # 현재의 min_값보다는 작으면
                min_ = now # min_ 값 수정
    else:
        visited[index] = 1 # 1로 처리하고
        dfs(index+1, now + employee[index] * visited[index])
        # 재귀입장 ( 인덱스 1 늘려주고, index번째 employee * visited 더해준다 )
        # 재귀에서 튕겨나왓을 때 이 위치로 돌아오는데 아래와 같이 visited[index]를 0으로 처리해줘야 전체 탐색 가능
        # ex) 가장 처음 부분집합은 1 1 1 1 1 여기서 index == N이 되므로 가장 마지막 1을 호출한 함수가 이 위치로 튕겨져 나옴
        visited[index] = 0
        # 이 함수의 index를 0으로 바꾸고
        dfs(index+1, now + employee[index] * visited[index])
        # 다시 재귀함수로 들어가야
        # 그 다음 부분집합인 1 1 1 1 0 을 탐색할 수 있음

for tc in range(1, int(input())+1):
    N, H = map(int, input().split())
    employee = list(map(int, input().split()))
    visited = [0]*N # 부분집합 표현할 리스트
    min_ = 99999999999999 # 최소값을 구해야하니 일단 매우 큰 수로 설정
    dfs(0, 0) # dfs 함수로 입장
    print('#{} {}'.format(tc, min_-H))








