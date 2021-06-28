for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    container.sort(reverse=True)
    truck.sort(reverse=True)

    visited = [False]*M

    total = 0
    for i in range(len(container)):
        for j in range(len(truck)):
            if container[i] <= truck[j] and visited[j] == False:
                total += container[i]
                visited[i] = True
                break
    print('#{} {}'.format(tc, total))