def check_(check):

    stack = []  # ()을 append, pop할 리스트
    for i in check: # 문자열을 돌면서
        if i == '(':  # (를 만나면
            stack.append('(')  # stack에 추가하고

        if i == ')':  # 만약 )를 만나면
            if len(stack) == 0:
                return 0
            elif stack[-1] == '{':  # 만약 현재 열려있는 괄호가 '{' 이면 오류이므로 그만!
                return 0
            stack.pop()  # A_list에서 제일 오른쪽 값을 pop한다

        # {} 도 똑같이 진행
        if i == '{':  # (를 만나면
            stack.append('{')  # stack에 추가하고

        if i == '}':  # 만약 }를 만나면
            if len(stack) == 0:
                return 0
            elif stack[-1] == '(':  # 만약 현재 열려있는 괄호가 '{' 이면 오류이므로 그만!
                return 0
            stack.pop()  # A_list에서 제일 오른쪽 값을 pop한ㄷ

    # check for문이 다 끝나고
    # A_list도 B_list도 비어있다면 짝이 다 잘 맞는 것이다
    if len(stack) == 0:
        return 1
    else:
        return 0


for tc in range(1, int(input())+1):
    C = input()  # check할 스트링문자
    print('#{} {}'.format(tc, check_(C)))


