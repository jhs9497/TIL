N = int(input())
arr = list(map(int, input().split()))

count = 0
for _ in range(N-1): # N-1만큼 단순반복
    for i in range(N-1): # i번쨰 친구랑 i+1자리의 친구를 비교해야하므로
                         # 전체 리스트 마지막에서 2번째까지만 for문 탐색
        if arr[i] > arr[i+1]: # 만약 현재 위치의 친구가 바로 다음 위치 친구보다 크면
            arr[i], arr[i+1] = arr[i+1], arr[i] # 자리 바꿔주기
            count += 1 # 자리 바꿔줄 때마다 카운트 + 1
        i+= 1
print(count)
