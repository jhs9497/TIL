def quick_sort(numbers, l, r):
    if l < r:
        s = partition(numbers, l, r)
        quick_sort(numbers, l, s-1)
        quick_sort(numbers, s+1, r)


def partition(numbers, l, r):
    p = numbers[l]
    i = l + 1
    j = r
    while i <= j:
        while(i <= j and numbers[i] <= p):
            i += 1
        while (i <= j and numbers[j] >= p):
            j -= 1
        if i <= j:
            numbers[i], numbers[j] = numbers[j], numbers[i]
    numbers[l], numbers[j] = numbers[j], numbers[l]
    return j


for tc in range(1, int(input())+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    quick_sort(numbers, 0, N-1)
    print('#{} {}'.format(tc, numbers[N//2]))