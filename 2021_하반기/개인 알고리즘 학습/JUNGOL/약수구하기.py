N, K = map(int, input().split())

count = 0
answer = 0
for i in range(1, N+1):
    if N % i == 0:
        answer = i
        count += 1

    if count == K:
        print(answer)
        break

if count < K:
    print('0')

