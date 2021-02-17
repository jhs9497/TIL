# 우선 100 X 100 배열 도화지를 만들자
coordi = [[0]*100 for _ in range(100)]

# 4번의 반복동안 저 도화지에 색칠하는거여

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    # 2차배열로 돌리면서 이 직사각형의 좌표를 도화지에 그린다
    # 단 현재 받은 좌표는 꼭짓점 좌표이므로 약간의 조정이 필요하다
    # 내가 편한 데이터로 만들기 위해서 
    # ex) 1 1 1
    #     1 1 1   이런 데이터가 있다하면 1의 갯수를 세고 넓이가 6이라 출력가능
    # x2, y2 데이터를 각각 -1씩 해주면 원하는 데이터로 사용할 수 있다.
    x1, y1, x2, y2 = x1, y1, x2-1, y2-1
    for i in range(x1, x2+1):  # 결국 range에 특성상 +1을 해줘서 그게 그거긴 해졌지만 개념은 다름
        for j in range(y1, y2+1):
            coordi[i][j] += 1

# 도화지 색칠이 다 끝나면
# 칠해진 2차원 도화지를 탐색하며 칠해져있으면 width에 1씩 추가
width = 0
for a in range(len(coordi)):
    for b in range(len(coordi)):
        if coordi[a][b] > 0:
            width += 1

print(width)




