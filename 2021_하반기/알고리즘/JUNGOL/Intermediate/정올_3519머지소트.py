def merge(A_list, left, mid, right):
    global B_list
    i = left
    j = mid + 1
    k = left
    # 작은 순서대로 배열에 삽입
    while i <= mid and j <= right:
        if A_list[i] <= A_list[j]:
            B_list[k] = A_list[i]
            i += 1
        else:
            B_list[k] = A_list[j]
            j += 1
        k += 1

    # 남은 데이터도 삽입
    # 1) i가 먼저 끝난 경우
    if i > mid:
        for t in range(j, right+1):
            B_list[k] = A_list[t]
            k += 1

    # 2) j가 먼저 끝난 경우
    else:
        for t in range(i, mid+1):
            B_list[k] = A_list[t]
            k += 1

    # 정렬된 배열을 삽입
    for t in range(left, right+1):
        A_list[t] = B_list[t]

def merge_sort(A_list, left, right):
    if left >= right:
        return

    mid = (left + right) // 2
    merge_sort(A_list, left, mid)
    print(f'{B_list}, left:{left}, right:{right}')
    merge_sort(A_list, mid+1, right)
    print(f'{B_list}, left:{left}, right:{right}')
    merge(A_list, left, mid, right)
    print(f'{B_list}, left:{left}, right:{right}')


N = int(input())
A_list = list(map(int, input().split()))
B_list = [0] * N
merge_sort(A_list, 0, N-1)
