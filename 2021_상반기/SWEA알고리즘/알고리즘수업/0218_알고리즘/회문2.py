import sys

sys.stdin = open("회문2.txt")

for tc in range(1):
    tc = int(input())
#     # 전체 보드를 만들고
    first_board = [list(input()) for _ in range(100)]
    # ['G','O','F','F'] 이런식으로 만들고 싶은데..
    str_board = [['']*100 for _ in range(100)]
    # 리스트를 스트링화해서 하나씩 새로운 str_board에 넣기
    for a in range(100):
        A = ''.join(first_board[a])
        for b in range(100):
            str_board[a][b] = A[b]

    # 죄다 검색
    answer = 0
    for M in range(100): # 직선파리채의 길이를 조절하는 것 직선파리채의 길이가 1부터 100까지 다 구해야하니깐

        for a in range(100): # 행or열을 의미

            for i in range(100-M+1): # 직선파리채에 따른 행or열의 범위
                # 행 후보군
                answer_R = []
                # 열 후보군
                answer_C = []

                for j in range(i, i+M):
                    answer_R += str_board[a][j]
                    answer_C += str_board[j][a]

                L = len(answer_R)

                if L % 2 == 1:  # N이 홀수라면
                    if answer_R[0:L // 2] == answer_R[L:L // 2:-1] and answer < L:
                        answer = L
                    if answer_C[0:L // 2] == answer_C[L:L // 2:-1] and answer < L:
                        answer = L
                else:
                    if answer_R[0:L // 2] == answer_R[L:L // 2 - 1:-1] and answer < L:
                        answer = L
                    if answer_C[0:L // 2] == answer_C[L:L // 2 - 1:-1] and answer < L:
                        answer = L

    print('#{} {}'.format(tc, answer))