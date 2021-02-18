for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
#     # N X N 글자판에서
#     # M길이의 회문을 찾아라
#
#     # 전체 보드를 만들고
    first_board = [list(input().split()) for _ in range(N)]
    # ['G','O','F','F'] 이런식으로 만들고 싶은데..
    str_board = [['']*N for _ in range(N)]
    # 리스트를 스트링화해서 하나씩 새로운 str_board에 넣기
    for a in range(N):
        A = ''.join(first_board[a])
        for b in range(len(A)):
            str_board[a][b] = A[b]

    # 행과 열 검색
    answer = []
    for a in range(N): # 0,1,2,3,4,5,6....19
     # N = 20, M = 13 라고 가정
        for i in range(N-M+1): # 0,1,2,3,4,5,6,7
            # 행 후보군
            answer_R = []
            # 열 후보군
            answer_C = []
            for j in range(i, i+M): # 7~20
                answer_R += str_board[a][j]
                answer_C += str_board[j][a]

            L = len(answer_R)

            if L % 2 == 1: # N이 홀수라면
                if answer_R[0:L//2] == answer_R[L:L//2:-1]:
                    answer = answer_R
                if answer_C[0:L//2] == answer_C[L:L//2:-1]:
                    answer = answer_C
            else:
                if answer_R[0:L//2] == answer_R[L:L//2-1:-1]:
                    answer = answer_R
                if answer_C[0:L // 2] == answer_C[L:L // 2 - 1:-1]:
                    answer = answer_C

    # 리스트 스트링화
    answer = ''.join(answer)

    print('#{} {}'.format(tc, answer))