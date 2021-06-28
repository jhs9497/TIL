for tc in range(1, int(input())+1):
    N = int(input())
    lst = list(map(int, input().split()))
    HEAP = [0]
    for data in lst:
        HEAP.append(data)

        pos = len(HEAP)-1
        # 최상위가 아닌동안 or 부모노드의 값이 data보다 작은 동안
        # 부모노드의 값과 현재 위치의 값을 변경한다.
        # 현재위치 <-> 부모노드위치 (pos = pos // 2)
        while pos > 1:
            if HEAP[pos] < HEAP[pos // 2]:
                HEAP[pos], HEAP[pos // 2] = HEAP[pos // 2], HEAP[pos]
            pos = pos // 2

    sumV = 0
    pos2 = len(HEAP)-1
    # 합구하기
    # 최상위가 아닌동안 or 부모노드의 값이 data보다 작은 동안
    # sumV += pos 값
    # 현재위치 <-> 부모노드위치 (pos = pos // 2)
    while pos2 > 1:
        sumV += HEAP[pos2 // 2]
        pos2 = pos2 // 2

    print('#{} {}'.format(tc, sumV))
