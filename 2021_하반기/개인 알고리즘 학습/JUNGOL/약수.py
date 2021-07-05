import math

N = int(input())
sqrt = int(math.sqrt(N))
arr = []

for i in range(1, sqrt+1):
    if N % i == 0:
        arr.append(i)
        if N // i != i:
            arr.append(N//i)

arr.sort()
print(*arr)

