from collections import deque

queue = deque()


queue.append(5)
queue.append(3)
queue.append(4)
queue.append(8)

queue.popleft()
print(*queue)