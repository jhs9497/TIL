def check(x, y, color):
    global answer

    # 우향, 우하향, 우상향, 하향
    dx = [0, 1, -1, 1]
    dy = [1, 1, 1, 0]

    for i in range(4):
        over_check_x = x - dx[i]  # x,y 뒤의 돌을 확인하기 위함
        over_check_y = y - dy[i]

        if 0 <= over_check_x < 19 and 0 <= over_check_y < 19 and badook[over_check_x][over_check_y] != color \
           or (over_check_x == -1 or over_check_y == -1 ):
            new_x = x + dx[i]
            new_y = y + dy[i]

            count = 1
            while 0 <= new_x < 19 and 0 <= new_y < 19 and badook[new_x][new_y] == color:
                count += 1
                new_x = new_x + dx[i]
                new_y = new_y + dy[i]

            if count == 5:
                answer = color
                return


badook = [list(map(int, input().split())) for _ in range(19)]

flag = 'open'
for i in range(len(badook)):
    for j in range(len(badook)):
        answer = 0
        if badook[i][j] == 1 or badook[i][j] == 2:
            check(i, j, badook[i][j])

        if answer != 0:
            flag = 'close'
            print(answer)
            print(i+1, j+1)
            break

    if flag == 'close':
        break


if flag == 'open':
    print(0)
