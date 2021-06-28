import random

A = []
for i in range(1, 51):
    A.append((i))

for _ in range(50):
    n = random.randrange(6, 11)
    k = random.randrange(1, n)
    print(n, k)
    for i in range(n):
        B = random.sample(A, n)
        print(*B)