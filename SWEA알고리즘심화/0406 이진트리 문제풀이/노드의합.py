for tc in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    # N == 노드의 개수
    # M == 리프노드의 개수
    # L == 출력할 노드 번호
    tree = [0] * (N+1)

    for i in range(M):
        idx, content = map(int, input().split())
        tree[idx] = content

    if N % 2 == 1:  # 총 노드 개수가 홀수면
        for i in range(len(tree)-1, 0, -1):
            if tree[i] == 0:
                tree[i] = tree[2*i] + tree[(2*i)+1]

    else: # 총 노드 개수가 짝수면
        tree[N // 2] = tree[N]
        # 맨 마지막 노드는 부모노드와 같은 값이므로 우선 처리해주고
        # 홀수일때보다 한 칸 앞에서 시작
        for i in range(len(tree)-2, 0, -1):
            if tree[i] == 0:
                tree[i] = tree[2*i] + tree[(2*i)+1]

    print('#{} {}'.format(tc, tree[L]))
