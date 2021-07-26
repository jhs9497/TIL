n, m = map(int, input().split())

Pascal = []

for i in range(1, n+1):
    temp = [-1] * i
    for j in range(i):
        if j == 0:
            temp[j] = 1
        elif j == i-1:
            temp[j] = 1
        else:
            temp[j] = Pascal[i - 2][j - 1] + Pascal[i - 2][j]

    Pascal.append(temp)

if m == 1:
    for i in Pascal:
        print(*i)

elif m == 2:
    count = 0
    for i in range(len(Pascal) - 1, -1, -1):
        row_pascal = ' '*count + ''
        for j in range(i+1):
            row_pascal += str(Pascal[i][j]) + ' '
        count += 1
        print(row_pascal)

elif m == 3:
    Pascal_copy = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i+1):
            Pascal_copy[i][j] = Pascal[i][j]


    New_pascal = [[0]*n for _ in range(n)]
    for i in range(len(New_pascal)):
        for j in range(len(New_pascal)):
            if i + j == n - 1:
                New_pascal[i][j] = Pascal_copy[i][j]
            else:
                New_pascal[i][j] = Pascal_copy[n - 1 - j][n - 1 - i]

    for i in range(len(New_pascal)):
        row_pascal = ''
        for j in range(len(New_pascal)):
            if New_pascal[i][j] != 0:
                row_pascal += str(New_pascal[i][j]) + ' '
        print(row_pascal)





        