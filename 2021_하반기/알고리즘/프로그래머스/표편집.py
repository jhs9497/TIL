def solution(n, k, cmd):
    answer = ['O' for _ in range(n)]
    up = ['blank'] + [x for x in range(n - 1)]
    down = [x for x in range(1, n)] + ['blank']
    delete_stack = []

    for command in cmd:
        c = command.split()
        if c[0] == 'U':
            count = int(c[1])
            for _ in range(count):
                k = up[k]

        elif c[0] == 'D':
            count = int(c[1])
            for _ in range(count):
                k = down[k]

        elif c[0] == 'C':
            delete_stack.append(k)
            answer[k] = 'X'

            # up[k]가 blank라는 뜻은
            # k가 현재 살아있는 리스트중 맨 위에 있다는 뜻
            # 삭제 후 아래에서 k재정의할 때 현재 k의 바로 아래칸으로 설정할 것이기 때문에
            # down[up[k]]를 설정하지 않아도 됨
            # down[k]도 마찬가지
            # 따라서 up[k], down[k]가 'blank'가 아닐 경우만 각각 체크하고 up, down 연결리스트를 업데이트해줌

            if up[k] != 'blank':
                # 만약에 k가 2 였고
                # up = ['blank', 0, 1, 2, 3, 4, 5, 6]
                # down = [1, 2, 3, 4, 5, 6, 7, 'blank'] 였으면
                # 2번째 노드가 사라지는 셈이니깐
                # down으로 2번째 노드로 향하는 친구를 바꿔줘야함
                # 즉 down[x] == 2 인 친구를 기존의 k가 down됐을 때 친구로 바꿔줘야함
                # 여기서 x를 구하는 방법은 기존의 k기준으로 한칸 위인 친구임
                # 그러므로 down[원래 k기준으로 한 칸 위에 있는 친구 (down일 시 k로 향했던 친구)] = 원래 k가 down됐을 때 친구로 설정
                down[up[k]] = down[k]

            if down[k] != 'blank':
                up[down[k]] = up[k]

            # 만약 기존의 k가 한 칸 더 내려갔을 때 blank면 맨 아래위치했다는 소리니깐 k를 기존의 k보다 한 칸 위로 설정하고
            # 아니면 기존의 k보다 한 칸 아래로 설정
            k = down[k] if down[k] != 'blank' else up[k]

        elif c[0] == 'Z':
            d = delete_stack.pop()
            answer[d] = 'O'

            # 위의 'C'와 로직은 같음 이번의 경우 회생시키는 것이니깐 지웠던 d를 넣어줌.
            if up[d] != 'blank':
                down[up[d]] = d

            if down[d] != 'blank':
                up[down[d]] = d

    ans = ''
    for a in answer:
        ans += a

    return ans