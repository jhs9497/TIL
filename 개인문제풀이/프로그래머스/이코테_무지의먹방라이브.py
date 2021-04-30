from queue import PriorityQueue

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    answer = 0
    q = PriorityQueue()
    for i in range(len(food_times)):
        q.put((food_times[i], i+1))
    sum_value = 0
    previous = 0
    length = len(food_times)
    while sum_value + ((q.queue[0][0] - previous) * length) <= k:
        now = q.get()[0]
        sum_value += (now - previous) * length
        length -= 1
    # 최대한 바퀴를 돌고 남은 음식들 중 몇 번째인지 확인
    target = k - sum_value + 1
    length = len(q.queue) # 남아있는 음식들
    temp = (target - 1) // length
    result = sorted(q.queue, key=lambda x:x[1])
    target -= temp * length
    return result[target - 1][1]