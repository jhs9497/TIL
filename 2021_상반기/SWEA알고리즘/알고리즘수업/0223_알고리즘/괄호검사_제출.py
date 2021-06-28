for tc in range(1, int(input())+1):
    check = input()

    A_list = []
    B_list = []

    now = ''
    ans = 0

    for i in check:
        if i == '(':
            A_list.append(1)
            now = '('

        if i == ')':
            A_list.pop()
            if now == '{':
                break

        if i == '{':
            A_list.append(1)
            now = '{'

        if i == '}':
            A_list.pop()
            if now == '(':
                break

    if len(A_list) == 0 and len(B_list) == 0:
        ans = 1

    print('#{} {}'.format(tc, ans))