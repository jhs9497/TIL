def danjo():
    naruto = 0  # 단조 초기값
    for a in range(len(A_list) - 1, 0, -1):  # 뒤에서 부터
        for b in range(a-1, -1, -1):
            #print(a)
            check = A_list[a] * A_list[b]
            print(check)
            if naruto >= check:  # 현 단조보다 체크할 값이 작으면 바로 버림
                break
            else:
                cnt = 0
                value = 10  # 나머지 초기값
                while check != 0:
                    if check % 10 <= value:  # 단조가 아니면 == 줄어들지 않으면
                        value = check % 10  # 줄어들어야하는 각 나머지값
                        check = check // 10  # 나눌값
                        cnt += 1
                        if cnt == len(str(A_list[a] * A_list[b])):
                            naruto = A_list[a] * A_list[b]
                            print(naruto)
                    else:
                        break
                  # 다 통과하면 처음에 곱한값이 단조 값
    return naruto


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    A_list = list(map(int, input().split()))

    # 단조 = 10으로 나눠가면서 나머지 = 뒤의 값부터 본다
    # 즉, 감소로 보는데, 같거나 작으면 다음꺼 나눠서 체크하고 아니면 바로 버림

    # 그 중 최댓값 - 거꾸로 가고, 현 최대값 단조보다 작으면 바로 거름

    naruto = danjo()
    if naruto == 0:
        print('#{} -1'.format(tc))
    else:
        print('#{} {}'.format(tc,naruto))