N = 5

snail = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

for i in range(1, N +1):

    snail[0][i-1] = i  # 1~5까지는 해결

C = N
number = N
while C > 0:

    if C % 2 == 1:

        C -= 1  # 우선 C = 4가 되겠지
        for a in range(N-C, C+1):  # 우선 C번씩 2번 반복 1~ 4
            number += 1
            snail[a][C] = number

        for b in range(C-1, N-C-2, -1):
            number += 1
            snail[C][b] = number

    else:  # C = 3

        C -= 1

        for c in range(C, N-C-2, -1):  # 3, 2, 1
            number += 1
            snail[c][N-C-1] = number

        for d in range(N-C-1, C+1): # 1, 2, 3
            number += 1
            snail[N-C-1][d] = number

print(snail)



