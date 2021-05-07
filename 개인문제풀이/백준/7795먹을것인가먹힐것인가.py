def search(A, B_list):
    left = 0
    right = len(B_list) -1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if B_list[mid] < A:
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    return result


for _ in range(int(input())):
    N, M = map(int, input().split())
    A_list = list(map(int, input().split()))
    B_list = list(map(int, input().split()))

    A_list.sort()
    B_list.sort()
    count = 0
    for A in A_list:
        count += search(A, B_list) + 1

    print(count)