# 입력은
# 4 5 -> 4X5의 판

# 2 3 1 5 4  -> 줄마다의 값
# 1 3 5 4 2
# 1 8 3 6 1
# 8 9 7 2 4

# 2 1 0 2 -> 초기 위치 2,1 의 점을 0쪽으로 2만큼 움직여라

# 0 = 오른쪽으로
# 1 = 왼쪽으로3 4
# 2 = 아래쪽으로
# 3 = 위쪽으로

N, M = map(int, input().split()) # 우선 N과 M값을 받고

# # 0으로 이루어진 NXM 짜리 보드판을 만들고
board = [list(map(int, input().split())) for _ in range(N)]

x, y, d, r = map(int, input().split()) # x, y = 좌표 / d = 가야할 방향 / r = 얼만큼 가는지

    # 움직임을 나타내는 함수를 만들자

up_down = [0, 0, 1, -1]
left_right = [1, -1, 0, 0]

# x+r*up_down[d]    # 만약 x,y 가 2,1 에  d가 0, r이 2라면 
# y+r*left_right[d]  # x,y 는 2,3 즉 오른쪽으로 2칸 가게 된다.

if x+r*up_down[d] < 0 or x+r*up_down[d] >= M or y+r*left_right[d] < 0 or y+r*left_right[d] >= N:
    print('범위를 벗어남 다시 입력하시오')

else:
    answer = board[x+r*up_down[d]][y+r*left_right[d]]

    print('답은 {}입니다.'.format(answer))








