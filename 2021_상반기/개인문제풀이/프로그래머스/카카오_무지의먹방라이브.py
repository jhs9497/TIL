# 처음부터 while문 떄리면 너무 오래 걸리니깐 최대한 음식리스트를 조작해서 후반부에 while문을 돌리자

def soultion(food_times, K):
    times = K // len(food_times) # 몇 바퀴 도는지
    rest = K % len(food_times)  # 음식이 충분할 경우 먹을 차례인 음식 번호 ( times만큼 돌고 나머지 )

    count = 0 # times만큼 도는 중에 0으로 변하는 친구들의 차를 누적 // 나중에 rest에 더해준다.
    for i in range(len(food_times)):
        if food_times[i] < times: # 이 경우면 times 바퀴 도는 동안 음식을 먼저 다 먹어버리게 됨
            food_times[i] = 0 # 우선 0으로 만들고
            count += (times - food_times[i]) # count에 차 만큼 더해준다. 나머지 돌릴때 더 돌려줘야함
        else: # food_times[i]가 작거나 같은 경우면
            food_times[i] -= times # 빼준다. times만큼 먹었을테니깐

    rest += count # rest에 더해주면서 while문을 돌릴 때 활용한다.

    # 현재 food_times는 예시로 치면 [2,0,1] 상태, rest는 2이다.
    idx = 0
    number = 0
    while number < rest:
        if food_times[idx] > 0:
            food_times[idx] -= 1
            number += 1 # 음식이 있을 때만 number +1
        idx += 1
        if idx >= len(food_times): # 만약 인덱스 넘어가면
            idx = 0 # 초기화
        if sum(food_times) == 0: # 만약 음식이 없으면
            return -1 # -1 리턴

    return idx+1 # 실제 인덱스값 +1 해서 리턴

food_times = list(map(int, input().split()))
K = int(input())

result = soultion(food_times, K)

