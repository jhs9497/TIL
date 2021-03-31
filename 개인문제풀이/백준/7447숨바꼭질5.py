from collections import deque

MAX_NUM = 500000
N, K = map(int, input().split())
# visited[n][0] : 짝수 시간에 위치 n을 방문한 최소시간
# visited[n][1] : 홀수 시간에 위치 n을 방문한 최소시간
visited = [[-1 for _ in range(MAX_NUM + 1)] for _ in range(2)]


def bfs():
    q = deque()
    q.append((N, 0))
    visited[0][N] = 0

    while len(q):
        n, cnt = q.popleft()
        # flag : cnt가 홀짝인지 결정
        flag = cnt % 2

        for next_n in [n + 1, n - 1, 2 * n]:
            if 0 <= next_n <= MAX_NUM and visited[1 - flag][next_n] == -1:
                # next_n 위치에는 cnt+1 시간에 방문할 것이니까.
                # 그런데 cnt+1 시간은 홀짝이 바뀌므로 1-flag로 해줌.
                visited[1 - flag][next_n] = cnt + 1
                q.append((next_n, cnt + 1))


# BFS : 먼저 가능한 모든 점을 방문하기.
bfs()

# 방문한 다음에 K를 늘려보면서 이 점에 방문할 수 있는지 확인하기.
t = 0
flag = 0
res = -1
while K <= 500000:
    if visited[flag][K] != -1:
        if visited[flag][K] <= t:
            res = t
            break
    flag = 1 - flag
    t += 1
    K += t

print(res)