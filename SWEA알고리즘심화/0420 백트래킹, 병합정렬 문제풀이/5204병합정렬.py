def merge_sort(m):
    global cnt
    if len(m) <= 1:
        return m

    mid = len(m) // 2
    left = merge_sort(numbers[:mid])
    right = merge_sort(numbers[mid:])

    return merge(numbers, left, right)

def merge(numbers, left, right):
    global cnt
    idxl = 0
    idxr = 0
    i = 0
    while idxl < len(left) and idxr < len(right):
        if left[idxl] < right[idxr]:
            numbers[i] = left[idxl]
            idxl += 1
        else:
            numbers[i] = right[idxr]
            idxr += 1
    if left[-1] > right[-1]: # 왼쪽 마지막 원소가 큰 경우
        cnt += 1
    if idxl < len(left): # 왼쪽 리스트가 남은 경우
        numbers[i:] = left[idxl:]
    return numbers


for tc in range(1, int(input())+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    cnt = 0
    numbers = merge_sort(numbers)
    print(numbers)