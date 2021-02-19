N, M = map(int, input().split())

first_board = [list(input().split()) for _ in range(N)]

str_board = [['']*N for _ in range(N)]

for a in range(N):
    A = ''.join(first_board[a])
    for b in range(len(A)):
        str_board[a][b] = A[b]

# N = 10, M = 10 이면 ?
answer = []
for a in range(N):    #0,1,2,3,4,5,6
    for i in range(M): # 0,1,2,3
        # 행 후보군
        answer_R = []
        # 열 후보군
        answer_C = []
        for j in range(i, i+M):  #
            answer_R += str_board[a][j]
            answer_C += str_board[j][a]

        print(answer_R)

# M = 7
# N = 4
# A = 'ABCDEFG'
#
# for i in range(N):
#     answer = ''
#     for j in range(i, N+i):
#         answer += A[j]
#     print(answer)