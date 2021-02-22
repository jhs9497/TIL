for tc in range(1, int(input())+1):
    first = input()
    A_list = list(map(int, input().split()))
    B_list = list(map(int, input().split()))

    # while 문을 이용하자

    # 선을 정해주고
    if first == 'A':
        A_goal = 1 # 초기 말의 위치
        B_goal = 1
        count = 0 # 진행 횟수이자 인덱스
        while A_goal < 20 and B_goal < 20 and count < 10: # 둘다 goal에 도착 못할 때하고 count도 10번이 안될 때만 진행
            A_goal += A_list[count] # A 먼저 진행
            if A_goal == B_goal: # 만약 A가 B를 잡으면
                B_goal = 1 # B는 초기화
            if A_goal >= 20: # 만약 A가 20을 넘기면
                print('#{} A'.format(tc))  # A 출력하고
                break # break

            B_goal += B_list[count] # 그 후 B 진행
            if B_goal == A_goal: # 만약 B가 A를 잡으면
                A_goal = 1 # A 초기화
            if B_goal >= 20:
                print('#{} B'.format(tc))
                break

            count += 1 # count 1 증가

        else:
            print('#{} AB'.format(tc))

    else: # B가 선이라면 반대로 진행
        A_goal = 1 # 초기 말의 위치
        B_goal = 1
        count = 0 # 진행 횟수이자 인덱스
        while A_goal < 20 and B_goal < 20 and count < 10: # 둘다 goal에 도착 못할 때하고 count도 10번이 안될 때만 진행
            B_goal += B_list[count]
            if B_goal == A_goal:
                A_goal = 1
            if B_goal >= 20:
                print('#{} B'.format(tc))
                break

            A_goal += A_list[count]
            if A_goal == B_goal:
                B_goal = 1
            if A_goal >= 20:
                print('#{} A'.format(tc))
                break

            count += 1
        else:
            print('#{} AB'.format(tc))
