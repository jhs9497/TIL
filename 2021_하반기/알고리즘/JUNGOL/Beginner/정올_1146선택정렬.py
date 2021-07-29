N = int(input())
number_list = list(map(int, input().split()))

idx = 0
while idx < N-1:
    min_number = min(number_list[idx:N])
    min_idx = 0
    for i in range(idx, N):
        if number_list[i] == min_number:
            min_idx = i
            break

    number_list[idx], number_list[min_idx] = number_list[min_idx], number_list[idx]

    idx += 1

    print(*number_list)
