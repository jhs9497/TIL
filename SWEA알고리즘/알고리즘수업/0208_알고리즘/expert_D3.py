# X = [0, 0, 3, 5, 2, 4, 9, 0, 6, 4, 0, 6, 0, 0]

test_case = int(input())

for i in range(1, test_case+1):
    Y = int(input())
    X = list(map(int, input().split()))


    X[0] = X[1] = X[-1] = X[-2] = 0

    total = 0
    for i in range(len(X)-4):

        a = X[i+2] - X[i]
        b = X[i+2] - X[i+1]
        c = X[i+2] - X[i+3]
        d = X[i+2] - X[i+4]

        A = [a, b, c, d]

        for a in A:
            min = 9999
            for b in range(len(A)):
                if A[b] < min:
                    min = A[b]
        if min > 0 :
            total += min

    print("#{} {}".format(test_case, total))
