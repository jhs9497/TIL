A = [3, 4, 5, 1, 2]

for i in range(len(A)):
    for j in range(len(A)-1):
        if A[j] > A[j+1]:
            A[j], A[j+1] =A[j+1], A[j]

print(A)

for a in range(len(A)):
    for j in range(len(A)-1):
        if A[j] < A[j+1]:
            A[j], A[j+1] =A[j+1], A[j]

print(A)
