import sys
sys.stdin = open("계산기3.txt")


for tc in range(1, 11):
    N = int(input())
    lst = list(input())

    num_lst = []

    for i in lst:
        if i == '(' or i == ')' or i =='+' or i =='*':
            num_lst.append(i)
        else:
            A = int(i)
            num_lst.append(A)

    # 후위 표기법을 변환하기
    stack = []
    cal = []  # 최종 후위표기법

    for i in num_lst:
        if i == '+': # '+'를 만났을 때
            if len(stack) == 0: # 만약 스택이 비어있으면
                stack.append(i)  # 스택에 추가

            elif stack[-1] == '*' or stack[-1] == '+': # 스택 맨 위가 '*' 이거나 '+' 이면
                cal.append(stack[-1]) # cal에 스택 맨위 연산기호 추가하고
                stack.pop() # 그 기호 없애주고
                if len(stack) > 0 and stack[-1] == '+':
                    cal.append(stack[-1])
                    stack.pop()

                stack.append(i) # 스택에 i 얹어주기

            elif '(' in stack: # 만약 '('이 스택 안에 있다면
                stack.append(i) # 스택에 추가

        elif i == '*':  # '*'를 만났을 때
            if len(stack) == 0:
                stack.append(i)

            elif stack[-1] == '*':
                cal.append(stack[-1])  # cal에 스택 맨위 연산기호 추가하고
                stack.pop()  # 그 기호 없애주고
                stack.append(i)  # 스택에 i 얹어주기

            elif '(' in stack or stack[-1] == '+':
                stack.append(i)


        elif i == '(':
            stack.append(i)

        elif i == ')':
            while stack[-1] != '(':
                cal.append(stack[-1])
                stack.pop()
            stack.pop() # '('까지 팝

        else:
            cal.append(i)

    if stack != []:  # 다 끝나고 만약 cal_list에 뭐가 있다면
        stack.reverse() # 뒤집고, why? 만약에 cal_list에 + * 이 남아있다면 number_list에는 * + 로 들어가야 하므로
        cal += stack # 더하기


    # 여기까지 후위표기식으로 완료

    ans_stack = []
    for i in cal:
        if i == '*':
            S = ans_stack[-2] * ans_stack[-1]
            ans_stack.pop()
            ans_stack.pop()
            ans_stack.append(S)

        elif i == '+':
            S = ans_stack[-2] + ans_stack[-1]
            ans_stack.pop()
            ans_stack.pop()
            ans_stack.append(S)

        else:
            ans_stack.append(i)

    print('#{} {}'.format(tc, ans_stack[0]))