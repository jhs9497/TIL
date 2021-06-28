test_case = int(input())

for tc in range(1, test_case+1):
    M, N = map(int, input().split())

    def cal(S, L):
        max_result = 0  # result 중 최댓값
        for i in range(len(L)-len(S)+1): # i는 S길이 만큼의 인덱싱의 시작점 0, 1, 2... 고정
            result = 0  # 한 번의 곱하기+더하기 결과가 나올때마다 저장 그리고 다시 for i 문을 돌며 0으로 초기화
            for j in range(len(S)): # j는 0,1,2 / 1,2,3 / 2,3,4 나와야함
                    result += S[j] * L[j+i]  # S는 0,1,2 고정이고 L은 변하며 나와야함

            if max_result < result:
                max_result = result

        print('#{} {}'.format(tc, max_result))


    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N > M :
        cal(A, B)
    else:
        cal(B, A)
