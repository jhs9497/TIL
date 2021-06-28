def check(X, count):
    global answer
    if visited[X] == True:
        if count >= answer:
            answer = count


    for x in range(len(info[X])):
        if visited[info[X][x]] == False:
            visited[info[X][x]] = True
            check(info[X][x], count+1)
            visited[info[X][x]] = False


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    info = [[] for _ in range(N+1)]
    for i in range(M):
        data = list(map(int, input().split()))
        info[data[0]].append(data[1])
        info[data[1]].append(data[0])
    print(info)

    if M == 0:
        print('#{} {}'.format(tc, '1'))
    else:
        answer = 0
        for j in range(1, N+1):
            visited = [False] * (N + 1)
            check(j, 0)
        print('#{} {}'.format(tc, answer))
