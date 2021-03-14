for tc in range(1, int(input())+1):
    N = int(input())
    Rc_car = []
    for _ in range(N):
        Rc_car.append(list(map(int, input().split())))

    total_distance = 0
    now_speed = 0
    for i in range(len(Rc_car)):
        if Rc_car[i][0] == 1: # 가속이면
            now_speed += Rc_car[i][1] # 현재 속도에 스피드값 더해주고
            total_distance += now_speed # 총거리에 추가

        elif Rc_car[i][0] == 2: # 감속이면
            now_speed -= Rc_car[i][1] # 현재 속도에서 스피드값 빼주고
            if now_speed < 0:
                now_speed = 0
            total_distance += now_speed # 총거리에 추가

        elif Rc_car[i][0] == 0: # 유지면
            total_distance += now_speed # 총거리에 현재 스피드만 추가

    print('#{} {}'.format(tc, total_distance))
