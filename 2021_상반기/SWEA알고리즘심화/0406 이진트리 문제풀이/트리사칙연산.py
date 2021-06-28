def check(root):
    global cal_list
    if root > 0:
        check(left_C[root])
        cal_list.append((tree[root], root))
        check(right_C[root])

for tc in range(1, 11):
    N = int(input())
    tree = [''] * (N+1)
    left_C = [0] * (N+1)
    right_C = [0] * (N+1)
    for i in range(N):
        inp = list(input().split())
        tree[int(inp[0])] = inp[1]

        if len(inp) > 2: # 연결정보 있다면 connect에 추가해주기
            left_C[int(inp[0])] = int(inp[2])
            right_C[int(inp[0])] = int(inp[3])

    cal_list = []
    check(1)

    root_idx = 0
    for i in range(len(cal_list)):
        if cal_list[i][1] == 1:
            root_idx = i
            break

    left_cal = int(cal_list[0][0]) # 왼쪽 서브트리에 가장 앞에 숫자 넣어놓고
    for i in range(1, root_idx): # 노드상 2부터 루트 전까지 돌면서
        if cal_list[i][0].isdigit(): # 만약 숫자면
            mathmath = cal_list[i-1][0]
            if mathmath == '+': # 만약 기호가 플러스면
                left_cal += int(cal_list[i][0])

            elif mathmath == '-':
                left_cal -= int(cal_list[i][0])

            elif mathmath == '*':
                left_cal *= int(cal_list[i][0])

            elif mathmath == '/':
                left_cal /= int(cal_list[i][0])


    right_cal = int(cal_list[root_idx+1][0]) # 오른쪽 서브트리에 가장 앞에 숫자 넣어놓고
    for i in range(root_idx+2, N): # 루트 다다음 노드 부터 끝까지 돌면서
        if cal_list[i][0].isdigit(): # 만약 숫자면
            mathmath = cal_list[i-1][0]
            if mathmath == '+': # 만약 기호가 플러스면
                right_cal += int(cal_list[i][0])

            elif mathmath == '-':
                right_cal -= int(cal_list[i][0])

            elif mathmath == '*':
                right_cal *= int(cal_list[i][0])

            elif mathmath == '/':
                right_cal /= int(cal_list[i][0])

    total = 0

    if cal_list[root_idx][0] == '+':
        total = left_cal + right_cal

    elif cal_list[root_idx][0] == '-':
        total = left_cal - right_cal

    elif cal_list[root_idx][0] == '*':
        total = left_cal * right_cal

    elif cal_list[root_idx][0] == '/':
        total = left_cal / right_cal

    print('#{} {}'.format(tc, int(total)))




