N = int(input())

arr = list(map(int, input().split()))

idx = 1
while idx < N:
    for i in range(0, idx):
        if arr[idx] < arr[i]:
            arr[idx], arr[i] = arr[i], arr[idx]
    idx += 1
    print(*arr)


