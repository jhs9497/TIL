N, M = map(int, input().split())

def dice(idx):
    for i in range(1, 7):
        arr[idx] = i
        if idx == N-1:
            if sum(arr) == M:
                print(*arr)
        else:
            dice(idx+1)

arr = [0] * N
dice(0)