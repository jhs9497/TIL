def DFS(x, y, number):

    if len(number) == 6: # 6자리 숫자가 완성되면
        answer.add(number) # set에 더해줄때는 add / list는 append
        return

    else:
        for i in range(4):
            r = x + dx[i]
            c = y + dy[i]
            if 0 <= r < 5 and 0 <= c < 5:
                DFS(r, c, number + board[r][c])
                # 숫자 이어가면서 재귀 DFS 입장

board = [list(input().split()) for _ in range(5)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = set() # set을 통해 자동 중복 제거

for i in range(5): # 2중 포문으로 모든 시작점 체크
    for j in range(5):
        number = board[i][j] # 초기 시작점 파라미터로 넘겨주기
        DFS(i, j, number)

print(len(answer)) # answer에 담겨있는 숫자들 갯수 프린트하면 끝!









