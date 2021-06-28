test_case = int(input())

for tc in range(1, test_case+1):
    M, N = map(int, input().split())

    def cal(S, L):
        max_result = 0
        for i in range(len(L)-len(S)+1):
            result = 0
            for j in range(len(S)):
                    result += S[j] * L[j+i]

            if max_result < result:
                max_result = result

        print('#{} {}'.format(tc, max_result))


    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N > M :
        cal(A, B)
    else:
        cal(B, A)