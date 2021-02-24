for tc in range(1, int(input())+1):
    N = int(input())
    number = [list(map(int, input().split())) for _ in range(N)]

    print('#{}'.format(tc))

    for i in range(N):
        for j in range(N):
            print(number[N-j-1][i], end="")
        print(" ", end="")
        for j in range(N):
            print(number[N-i-1][N-j-1], end="")
        print(" ", end="")
        for j in range(N):
            print(number[j][N-i-1], end="")
        print()






