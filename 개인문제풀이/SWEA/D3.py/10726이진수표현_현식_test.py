def check(N, M):
    if M == 0:
        return 'OFF'
    count = 0
    number = M
    while count < N:
        if number % 2 == 0:
            return 'OFF'
        number = number // 2
        count += 1
    return 'ON'


T = int(input())
answer = []
for tc in range(T):
    N, M = map(int, input().split())
    answer.append(check(N,M))

for i in range(T):
    print("#{} {}".format(i+1, answer[i]))