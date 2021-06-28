def combi(deep, start):
    if deep == K:
        print(A)
    else:
        for i in range(start, 5 - K + deep + 1):
            A[deep] = B[i]
            combi(deep + 1, i + 1)

K = 3
B = [1,2,3,4,5]
A = [0] * K
combi(0,0)