

def itoa_(N):
    if N >= 0:
        S = []
        while  N > 0:
            s = N % 10
            S += [s]
            N = N // 10
        answer = []
        for i in range(len(S)-1, -1, -1):
            answer += S[i]
        print(answer, type(answer))

    else:
        S = []
        N = N * -1
        while  N > 0:
            s = N % 10
            S += [s]
            N = N // 10
        answer = ''
        for i in range(len(S)-1, -1, -1):

        print(answer, type(answer))

itoa_(1564)

