N = int(input())
arr = list(map(int, input().split()))
Max_count = 0
for i in range(len(arr)-1):
    count_up = 1
    count_down = 1
    for j in range(i, len(arr)-1):
        if arr[j] <= arr[j+1]:
           count_up += 1
        else:
           count_up = 1

        if arr[j] >= arr[j+1]:
            count_down += 1
        else:
            count_down = 1

    if Max_count < count_up:
        Max_count = count_up

    if Max_count < count_down:
        Max_count = count_down

