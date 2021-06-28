from collections import deque
def solution(bridge_length, weight, truck_weights):

    B = [0] * bridge_length  # 길이가 2인 다리 표현
    B = deque(B)
    W = weight  # 10
    sec = 0 # 초
    truck = deque(truck_weights)  # 시간 초과가 떠서 deque활용 // 그래도 시간초과..

    while len(truck) > 0: # deque로 받은 트럭이 다 건너기 전까지

        sec += 1  # while문 한 번 돌때마다 1초씩 추가
        if sum(B) <= W:  # 만약 다리위의 트럭 총합이 W보다 낮을때
            B.popleft()  # 우선 앞에 날리고
            B.append(0) # 다리 맨 뒤는 0 추가로 마치 앞으로 한칸씩 움직인 효과
            # 처음에 이 초기화를 위에 for문 안에 넣었다가 다리길이가 1인경우 for문에 입장을 못해서 에러 났었음
            if W - sum(B) >= truck[0]: # 만약 총 무게 - 다리위 트럭 무게가 현재 대기줄 맨 앞 트럭 무게보다 크거나 같다면
                B[-1] = truck[0] # 다리에 입장
                truck.popleft() # 대기줄 맨 앞 트럭 pop

    return sec + bridge_length # 다리길이를 더하는 이유는 트럭 대기줄에서 마지막 트럭이 다리에 오르는 순간
                               # while문이 종료 되기 때문에 마지막 트럭이 다리를 건너는 초를 더해줘야한다

print(solution(5, 5, [2,2,2,2,1,1,1,1,1]))

