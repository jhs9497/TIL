for tc in range(1, int(input())+1):
    blueprint = list(input())

    # () 를 레이저로 바꿔주기
    for i in range(len(blueprint)-1):
        if blueprint[i] == '(':
            if blueprint[i+1] ==')':
                blueprint[i] ='R'
                blueprint[i+1] = ' '  # 공백으로 바꾸고 활용하진 않을거임

    stick_count = 0 # 총 쇠막대 수
    damage_count = 0 # 레이저 쏘인 수
    stick_now = 0 # 현재 시점 쇠막대 수

    for i in range(len(blueprint)):
        # 쇠막대의 시작점 '('를 만나면 총 막대수에 += 1 , 현재 시점 쇠막대 수에 += 1
        if blueprint[i] == '(':
            stick_count += 1
            stick_now += 1

        # 레이저를 만나면 레이저 쏘인 수에 현재 열려있는 쇠막대수 더해주기
        elif blueprint[i] == 'R':
            damage_count += stick_now

        # 그리고 현재 시점 쇠막대 수 -= 1
        elif blueprint[i] ==')':
            stick_now -= 1

    # 최종 잘린 쇠토막은 쇠가 맞은 횟수 + 잘리기 전 처음 쇠막대의 갯수
    result = damage_count + stick_count

    print('#{} {}'.format(tc, result))
