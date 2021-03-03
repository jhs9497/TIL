from collections import deque

def solution(prices):

    P = deque(prices)
    answer = []

    while P :
        if min(P) == P[0]:  # 만약 가격이 떨어지지 않는 경우면
            sec = 0
            for i in range(1, len(P)):
                if P[0] <= P[i]:
                    sec += 1
                else:
                    break
            P.popleft()
            answer.append(sec)
        else:
            sec = 1 # 예시에서 3 -> 2로 곧바로 떨어져도 1초유지라 하였으므로 sec= 1부터 시작
            for i in range(1, len(P)):
                if P[0] <= P[i]:
                    sec += 1
                else:
                    break
            P.popleft()
            answer.append(sec)
    return answer
print(solution(prices))