# 우선 100 X 100 보드판을 만들고
board = [[0]*100 for _ in range(100)]

N = int(input())

for _ in range(N):
    x, y = map(int, input().split())
    # x, y를 -1씩 해준다! board판이 인덱스가 0부터 시작하니깐!
    x, y = x-1, y-1
    # x ~ x+10, y ~ y + 10 을 돌면서 0으로 이루어진 board판에 1을 칠해준다
    for i in range(x, x+10):
        for j in range(y, y+10):
            board[i][j] = 1

count = 0
for a in range(100):
    for b in range(100):
        # 다시 한번 보드판을 돌면서 만약 1이면 칠해졌단 소리니깐 그걸 카운팅해서 답 도출
        if board[a][b] == 1:
            count += 1

print(count)