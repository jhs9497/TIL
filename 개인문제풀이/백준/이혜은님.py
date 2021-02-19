def bingo():

    i = 0
    while i < N:
        total1, total2, total3, total4 = 0, 0, 0, 0
        for j in range(N):
            if j < N and arr[i][j] == 'o':
                total1 += 1
            else:
                total1 = 0

            if total1 == 5:
                return "Yes"

            if j < N and arr[j][i] == 'o':
                total2 += 1
            else:
                total2 = 0

            if total2 == 5:
                return "Yes"

            # if j < N and arr[j][j] == 'o':
            #     total3 += 1
            # else:
            #     total3 = 0
            #
            # if total3 == 5:
            #     return "Yes"
            #
            # if j < N and arr[j][N-1-j] == 'o':
            #     total4 += 1
            # else:
            #     total4 = 0
            #
            # if total4 == 5:
            #     return "Yes"

        i += 1

    return "NO"


for tc in range(1, int(input())+1):

    N = int(input())
    arr = [input() for _ in range(N)]
    print("#{} {}".format(tc, bingo()))