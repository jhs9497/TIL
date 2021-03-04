for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    # N -> 화덕 크기
    oven = [[-1] for _ in range(N)]  # 화덕에 피자를 표현할 곳
    baked_idx = [] # 완성된 피자idx 순서를 표현할 곳
    p_pizza = list(map(int, input().split()))

    pizza = []  # pizza의 치즈양과 인덱스 동시에 표현
    for i in range(M):
        pizza.append([p_pizza[i], i])


    while len(baked_idx) < M: # 완성된 피자수가 전체 피자수보다 작을 동안
        for i in range(len(oven)):
            if oven[i] == [-1] and pizza: # oven의 i가 빈공간이고 만약 대기 피자가 남아있다면
                oven[i] = pizza[0] # 피자 추가
                pizza.pop(0) # 추가한거 날리기

            oven[i][0] = oven[i][0] //2 # 치즈 녹이기

            if oven[i][0] == 0: # 만약 피자가 다 녹았으면
                baked_idx.append(oven[i][1]) # 완성피자에 인덱스 추가해주고
                oven[i] = [-1] # oven은 -1로 바꿔서 비어있음을 표현

    # 완성 빵에 맨 마지막 인덱스를 출력하면 되는데 인덱스이므로 +1 해서 출력하기
    print('#{} {}'.format(tc, baked_idx[-1]+1))





