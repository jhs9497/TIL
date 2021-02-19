for tc in range(1, int(input())+1):
    S_str = input()
    L_str = input()

    answer = 0
    for i in range(len(S_str)):
        count = 0
        for j in range(len(L_str)):
            if S_str[i] == L_str[j]:
                count += 1
        if answer < count:
            answer = count

    print('#{} {}'.format(tc, answer))