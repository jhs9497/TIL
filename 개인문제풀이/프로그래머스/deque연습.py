from collections import deque



B = [1,2,3,4,6]

A = deque(B)

print(A, type(A))

A.popleft()

print(A)
print(len(A))
print(A[2])