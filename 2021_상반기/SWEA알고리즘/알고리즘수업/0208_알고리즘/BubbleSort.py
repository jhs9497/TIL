X = [55, 7, 78, 12, 42]

def BubbleSort(A):

    for j in range(len(A)-1, 0, -1):
            if A[i] > A[i+1]:
        for i in range(j):
                A[i], A[i+1] = A[i+1], A[i]
BubbleSort(X)

print(X)