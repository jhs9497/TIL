N, K = map(int, input().split())

Queue = []
for i in range(1, N+1):
    Queue.append(i)
idx = K-1
while len(Queue) > 1:
    if idx < len(Queue):
        Queue.pop(idx)
    else:
        idx = idx % len(Queue)
        Queue.pop(idx)
    idx += K-1

print(Queue[0])
