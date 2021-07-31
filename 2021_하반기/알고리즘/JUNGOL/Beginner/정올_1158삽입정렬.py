N = int(input())

arr = list(map(int, input().split()))

idx = 1
while idx < N: # idx가 N보다 작을때 반복
    for i in range(0, idx): # 리스트의 맨 처음 ~ idx까지 보면서
        if arr[idx] < arr[i]: # idx위치의 친구보다 큰 친구를 마주치면
            arr[idx], arr[i] = arr[i], arr[idx] # 둘의 자리 바꿔주기
    idx += 1
    print(*arr) # 시행마다 과정 출력


