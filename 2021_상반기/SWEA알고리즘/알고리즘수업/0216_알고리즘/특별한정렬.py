test_case = int(input())


for tc in range(1, test_case+1):
    N = int(input())
    number = list(map(int, input().split()))

    for a in range(N-1):
        for b in range(N-1):
            if number[b] > number[b+1]:
                number[b], number[b+1] = number[b+1], number[b]


    # 반으로 나누자 N이 짝수일때 홀수일때 나눠서
    if N % 2 == 0:

        small_number = number[0:N//2]   # 작은수부터 정배열
        large_number = number[N:N//2-1:-1]  # 큰수부터 역배열

    else:
        small_number = number[0:N//2+1]   # 작은수부터 정배열
        large_number = number[N:N//2-1:-1]  # 큰수부터 역배열

    # 답이 되는 리스트공간
    answer_list = [0]*10

    for i in range(10):
        if i == 0 or i % 2 == 0:
            answer_list[i] = large_number[i//2]
        # i가 짝수이면
        # 0 2 4 6 8은
        # large_number에 0 1 2 3 4
        else:
            answer_list[i] = small_number[(i-1)//2]
        # i가 홀수이면
        # 1 3 5 7 9는
        # small_number에 0 1 2 3 4

    # 형식에 맞게 list 스트링화

    answer_str = ''

    for S in answer_list:
        answer_str += str(S)
        answer_str += ' '

    print("#{} {}".format(tc, answer_str))


