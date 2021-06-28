A = input()
B = set(A)
C = list(B)
D = [0]*len(C)

for i in range(len(A)):
    for j in range(len(C)):
        if A[i] == C[j]:
            D[j] += 1


