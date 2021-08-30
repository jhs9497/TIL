N = int(input())
N_list = list(map(int, input().split()))
Q = int(input())
Q_list = list(map(int, input().split()))

def check(start, end, target):
    global N_list
    while start <= end:
        mid = (start + end) // 2
        if N_list[mid] == target:
            return mid
        if N_list[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return -1

for q in Q_list:
    result = check(0, N-1, q)
    print(result, end=" ")