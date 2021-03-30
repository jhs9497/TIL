for tc in range(1, int(input())+1):
    button = list(input().split())
    O = [1] # 초기 로봇 위치
    B = [1]
    for i in range(len(button)-1):
        if button[i] =='O':
            O.append(int(button[i+1]))
        if button[i] =='B':
            B.append(int(button[i+1]))

    O_sec = len(O)-1 # 스위치 갯수로 초기값
    for i in range(len(O)-1):
        O_sec += abs(O[i+1] - O[i])

    B_sec = len(B)-1 # 스위치 갯수로 초기값
    for i in range(len(B)-1):
        B_sec += abs(B[i+1] - B[i])

    if O_sec > B_sec:
        print('#{} {}'.format(tc, O_sec))
    else:
        print('#{} {}'.format(tc, B_sec))