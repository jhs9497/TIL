def check(x,y):
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]

    for i in range(8):
        cnt = 1
        new_x = x + dx[i]
        new_y = y + dy[i]
        door = 'open'
        while door == 'open' and 0 <= new_x < N and 0 <= new_y < N:

            if 0 <= new_x < N and 0 <= new_y < N and omok[new_x][new_y] =='o':
                cnt += 1
                new_x = new_x + dx[i]
                new_y = new_y + dy[i]
                if cnt == 5:
                    return 'YES'
            else:
                door = 'close'

    return 'NO'

for tc in range(1, int(input())+1):
    N = int(input())
    omok = [list(input()) for _ in range(N)]

    answer = 'NO'
    for i in range(N):
        for j in range(N):
            if omok[i][j] =='o':
                answer = check(i,j)
            if answer == 'YES':
                break
        if answer == 'YES':
            break


    print('#{} {}'.format(tc, answer))
