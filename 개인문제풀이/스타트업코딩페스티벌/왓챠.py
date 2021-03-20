score = list(map(float, input().split()))
grade = ['A', 'B', 'C', 'D', 'E']

my_dict = {}

for i in range(5):
    my_dict[score[i]] = grade[i]

score.sort(reverse=True)

prefer = []

for i in range(5):
    prefer.append(my_dict[score[i]])


N, M = map(int, input().split())

board_watch = [list(input()) for _ in range(N)]
board_grade = [list(input()) for _ in range(N)]

result = []

my_dict_2 = {}
for i in range(5):
    my_dict_2[prefer[i]] = score[i]

for i in range(N):
    for j in range(M):
        board_grade[i][j] = my_dict_2[board_grade[i][j]]


for i in range(N):
    for j in range(M):
        if board_watch[i][j] == 'Y' and board_grade[i][j] == score[0]:
            result.append((i,j))

for i in range(N):
    for j in range(M):
        if board_watch[i][j] == 'Y' and board_grade[i][j] == score[1]:
            result.append((i,j))

for i in range(N):
    for j in range(M):
        if board_watch[i][j] == 'Y' and board_grade[i][j] == score[2]:
            result.append((i,j))

for i in range(N):
    for j in range(M):
        if board_watch[i][j] == 'Y' and board_grade[i][j] == score[3]:
            result.append((i,j))

for i in range(N):
    for j in range(M):
        if board_watch[i][j] == 'Y' and board_grade[i][j] == score[4]:
            result.append((i,j))


for i in range(N):
    for j in range(M):
        if board_watch[i][j] == 'O' and board_grade[i][j] == score[0]:
            result.append((i,j))

for i in range(N):
    for j in range(M):
        if board_watch[i][j] == 'O' and board_grade[i][j] == score[1]:
            result.append((i,j))

for i in range(N):
    for j in range(M):
        if board_watch[i][j] == 'O' and board_grade[i][j] == score[2]:
            result.append((i,j))

for i in range(N):
    for j in range(M):
        if board_watch[i][j] == 'O' and board_grade[i][j] == score[3]:
            result.append((i,j))

for i in range(N):
    for j in range(M):
        if board_watch[i][j] == 'O' and board_grade[i][j] == score[4]:
            result.append((i,j))




for X in result:
    answer = ''
    answer += my_dict[board_grade[X[0]][X[1]]]
    answer += ' '
    answer += str(board_grade[X[0]][X[1]])
    answer += ' '
    answer += str(X[0])
    answer += ' '
    answer += str(X[1])
    print(answer)
