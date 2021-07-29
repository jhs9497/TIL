N = int(input())
arr = list(map(int, input().split()))

count = 0
for _ in range(N-1):
    for i in range(N-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            count += 1
        i+= 1
print(count)
