def tree(root):
    global count
    if root > 0:
        count += 1
        tree(left_C[root])
        tree(right_C[root])

for tc in range(1, int(input())+1):
    E, N = map(int, input().split())
    info = list(map(int, input().split()))
    left_C = [0] * (E+2)
    right_C = [0] * (E+2)

    turn = -1
    for i in range(0, len(info), 2):
        if turn == info[i]: # 위에 turn이 지금 내 값이랑 같다는 것은 오른쪽 노드에 촤일드를 추가해야한다는 뜻!
            right_C[info[i]] = info[i+1]
        else:
            left_C[info[i]] = info[i+1]
            turn = info[i] # 턴에 나는 왼쪽에 한 번 추가했어~! 의미 부여

    count = 0
    tree(N)
    print('#{} {}'.format(tc, count))


