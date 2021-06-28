N, K = map(int, input().split())

count = 0

# 나눌 수 있을땐 최대한 나눈다!
while N >= K:
    # N이 K로 나누어 떨어지지 않는다면 N에 -1해주기
    while N % K != 0:
        N -= 1
        count += 1
    N = N // K
    count += 1

# 만약 위 while문을 통과하고 N이 1과 K사이에 위치해 있다면 -1 해줘야 한다.
while N > 1:
    N -= 1
    count += 1

print(count)
