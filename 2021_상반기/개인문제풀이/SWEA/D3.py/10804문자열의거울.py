T = int(input())
for tc in range(1, T+1):
    sample = list(input())
    A_sample = sample[::-1]

    for i in range(len(A_sample)):
        if A_sample[i] == 'b':
            A_sample[i] = 'd'
        elif A_sample[i] == 'd':
            A_sample[i] = 'b'
        elif A_sample[i] == 'q':
            A_sample[i] ='p'
        elif A_sample[i] =='p':
            A_sample[i] = 'q'

    answer = ''
    for i in range(len(A_sample)):
        answer += A_sample[i]

    print('#{} {}'.format(tc, answer))
