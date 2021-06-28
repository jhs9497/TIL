for tc in range(1, int(input())+1):
    N = int(input())
    numbers = []
    cnt = 0 # 횟수
    X = 1 # N의 배수를 조절
    while len(numbers) < 10:
        numbers = list(numbers) # 다시 리스트로
        N_N = X*N # 밑에 while문에서만 쓸 N값
        while N_N > 0: # N_N이 0보다 큰 동안에
            if N_N < 10: # 만약 N_N이 1의자리면
                numbers.append(N_N) # 그냥 추가해주고
            else: # 1의 자리가 아니면
                numbers.append(N_N%10) # 10으로 나눈 나머지를 추가해주고
            N_N = N_N // 10 # N은 10으로 나눈 몫
        X += 1
        numbers = set(numbers) # set으로 중복 없애기
    
    X -= 1
    print('#{} {}'.format(tc, X*N))ee