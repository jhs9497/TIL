def back(X, Y, P, Count):
    global total
    if Count == number: # 만약 N번만큼 돌았으면 -> 겹치지 않고 pure하게 왔으면
        total += P # 지금까지 축적된 P 더해주기
        return
    Now = P
    ground[X][Y] = 1 # 현재 좌표 방문체크
    for i in range(4):
        NEW_X = X + dx[i]
        NEW_Y = Y + dy[i]
        if 0 <= NEW_X < 2*number+1 and 0 <= NEW_Y < 2*number+1:
            if ground[NEW_X][NEW_Y] == 1: # 만약 방문체크 했던 곳이면
                continue # 넘어가고
            else: # 방문안한 경우에만
                back(NEW_X, NEW_Y, Now*percent[i], Count+1)
                ground[NEW_X][NEW_Y] = 0

number, E, W, S, N = map(int, input().split())

percent = [E/100, W/100, S/100, N/100]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

ground = [[0]*(2*number+1) for _ in range(2*number+1)] # 미친 로봇이 돌아다닐 수 있는 운동장 크기
                                       # 한쪽으로만 N번을 간다면 그게 최대 범위 -> 4방을 고려해야하니 2N 2N , 인덱스니깐 + 1

total = 0

back(number, number, 1, 0) # N,N이 ground의 가운데이자 로봇의 최초지점, 1은 곱해나갈 확률 (최초니깐 1으로 설정), 횟수

print(total)