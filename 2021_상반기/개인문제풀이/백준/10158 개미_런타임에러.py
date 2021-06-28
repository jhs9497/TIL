w, h = map(int, input().split())
x, y = map(int, input().split())
t = int(input())

# 위에서부터 아래로 떨어지는 우리가 아는 2차원배열로 풀어도 같은 정답이 나올듯 하다

# while을 이용하자
# 우선 시작은 위로 45도 방향 고정이니 x-d, y_d = 1
x_d = 1
y_d = 1
count = 0
while count < t :
    if x == w :  # x가 w와 같아졌을 때

        if y_d < 0 : # 좌하향 방향으로 오고 있었다면 y_d < 0 , x_d > 0 이란 뜻
            x_d = x_d * -1  # x, y 둘다 마이너스로 가야하므로 x_d 만 * -1
        else: # 우상향 방향으로 오고 있었다면 y_d > 0, x_d > 0 이란 뜻
            x_d = x_d * -1 # x만 마이너스로 가야하므로 x_d 만 * -1


    elif x == 0 : # x가 0일 때
        # 좌상향 방향으로 오고 있었다면
        if y_d > 0 : # x_d < 0, y_d > 0 이란 뜻
            x_d = x_d * -1  # x는 -, y 는 + 로
            y_d = y_d * -1
        else: # 좌하향 방향으로 오고 있었다면 x_d, y_d 모두 -1 이란 뜻
            x_d = x_d * -1  # 다음 움직임은 둘다 플러스로 가야함
            y_d = y_d * -1


    elif y == h:  # y가 h랑 같아졌을 때
        if x_d < 0 : # 좌상향 방향으로 오고 있었다면 x_d < 0 , y_d > 0 이란 뜻
            y_d = y_d * -1 # 둘다 마이너스로 가야하므로 y만 * -1
        else: # 우상향 방향으로 오고 있었다면  # x_d > 0, y_d > 0 이란 뜻
            y_d = y_d * -1 # y만 마이너스로 가야함

    elif y == 0 : # 만약 y가 0일 때
        if y_d < 0 :
            y_d = y_d * -1
        else:
            y_d = y_d * -1

    x = x + x_d  # 위에서 설정된 방향대로 움직인다
    y = y + y_d
    count += 1
print(x, y)
