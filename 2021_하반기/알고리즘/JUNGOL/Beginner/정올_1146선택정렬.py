N = int(input())
number_list = list(map(int, input().split()))

idx = 0
while idx < N-1: # idx가 리스트의 끝까지 올때까지 반복
    min_number = min(number_list[idx:N]) # idx~끝까지의 리스트중 가장 작은 수 도출
    min_idx = 0
    for i in range(idx, N): # idx~끝까지 체크하면서
        if number_list[i] == min_number: # min_number랑 같은 친구 만나면
            min_idx = i # 그 인덱스값을 min_idx에 저장
            break
    # idx~N까지의 리스트중 맨 앞자리인 idx위치의 숫자와 min_idx위치의 숫자 바꿔주기
    number_list[idx], number_list[min_idx] = number_list[min_idx], number_list[idx]

    idx += 1

    print(*number_list)
