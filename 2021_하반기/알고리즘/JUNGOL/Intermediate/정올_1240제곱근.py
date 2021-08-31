N = int(input())

start = 1
end = N // 2

def check(start, end):
    if N == 1:
        return 1
    mid = (start + end) // 2
    if mid**2 <= N < (mid+1) **2:
        return mid

    if mid**2 < N:
        return check(mid+1, end)
    else:
        return check(start, mid-1)

answer = check(start, end)
print(answer)