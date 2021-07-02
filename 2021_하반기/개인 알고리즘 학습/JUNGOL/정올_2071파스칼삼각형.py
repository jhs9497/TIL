n, m = map(int, input().split())

answer = []

for i in range(1, n+1):
    temp = [-1] * i
    for j in range(i):
        if j == 0:
            temp[j] = 1
        elif j == i-1:
            temp[j] = 1
        else:
            temp[j] = answer[i-2][j-1] + answer[i-2][j]

    answer.append(temp)

if m == 1:
    for i in answer:
        print(*i)

elif m == 2:
    count = 0
    for i in range(len(answer)-1, -1, -1):
        pascal = ' '*count + ''
        for j in range(i+1):
            pascal += str(answer[i][j]) + ' '
        count += 1
        print(pascal)

elif m == 3:
    board = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1):
            board[i][j] = answer[i][j]

    New_pascal = [[0]*n for _ in range(n)]
    for i in range(len(New_pascal)):
        for j in range(len(New_pascal)):
            print(board[i][j])