def search(X, Y, P, Count):
    global total
    if Count == number: # 만약 N번만큼 돌았으면 -> 한 번도 겹치는 곳 없이 무사도착했으면
        total += P # 지금까지 축적된 P 더해주기
        return

    Now = P # Now는 건네받은 확률을 담은 변수
    ground[X][Y] = 1 # 현재 좌표 방문체크
    for i in range(4):
        NEW_X = X + dx[i] # 한 칸 움직이고
        NEW_Y = Y + dy[i]
        if 0 <= NEW_X < 2*number+1 and 0 <= NEW_Y < 2*number+1: # 이 가정은 필요없을수도 ? 습관상 해버림..
            if ground[NEW_X][NEW_Y] == 1: # 만약 방문체크 했던 곳이면
                continue # 넘어가고
            else: # 방문안한 경우에만
                search(NEW_X, NEW_Y, Now*percent[i], Count+1) # 재귀로 함수 진입
                ground[NEW_X][NEW_Y] = 0 # 함수가 리턴되서 튕겨나왔을 때 현재 지점의 방문체크는 0으로 돌려놔야 정확하게 탐색가능

number, E, W, S, N = map(int, input().split())

percent = [E/100, W/100, S/100, N/100] # 입력받은 동서남북의 확률퍼센트를 수치화

dx = [0, 0, 1, -1] # 퍼센트에 맞춰서 동서남북으로
dy = [1, -1, 0, 0]

ground = [[0]*(2*number+1) for _ in range(2*number+1)] # 미친 로봇이 돌아다닐 수 있는 운동장 크기
                            # 한쪽으로만 N번을 간다면 그게 최대 범위 -> 4방을 고려해야하니 초기 나자신 위치 더해줘서 2N+1, 2N+1

total = 0 # 퍼센트들을 다 더해서 최종적으로 프린트할 변수

search(number, number, 1, 0) # N,N이 ground의 가운데이자 로봇의 최초지점, 1은 곱해나갈 확률 (최초니깐 1으로 설정), 횟수

print(total)



