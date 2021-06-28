import sys
sys.stdin = open("계산기.txt")


for tc in range(1, 11):
    L = int(input())
    number = input()

    # 후위로 표현 먼저

    cal_list = []  # 연산기호 넣을 곳
    number_list = []  # 후위표기법으로 표기할 곳
    for i in number:
        if i == '+':  # +를 만났을 때
            if cal_list == []:  # cal_list에 아무것도 없다면
                cal_list.append('+')
            elif cal_list != [] :  # 만약 cal_list에 뭐라도 있으면
                number_list.append(cal_list[-1]) # 후위표기리스트에 추가하고
                cal_list.pop()  # 있던건 pop!
                if cal_list != []: # 이 상황에서 아직 '+'가 밑에 남아있으면 cal_list에 3개이상 쌓이는 경우는 + * + 밖에 없음
                    if cal_list[0] == '+':
                        number_list.append('+') # + 추가하고
                        cal_list.pop()  # pop!

                cal_list.append('+') # 모든 체킹 끝나고 마지막에 추가

        elif i == '*': # *를 만났을 때
           if cal_list == []:
               cal_list.append('*')
           else:
               if cal_list[-1] == '+':
                   cal_list.append('*')
               else:
                   number_list.append('*')
        else: # 숫자면
            number_list.append(int(i))  # int화 해서 number_list에 추가

    if cal_list != []:  # 다 끝나고 만약 cal_list에 뭐가 있다면
        cal_list.reverse() # 뒤집고, why? 만약에 cal_list에 + * 이 남아있다면 number_list에는 * + 로 들어가야 하므로
        number_list += cal_list # 더하기

    # 여기까지 후위표기법으로 number_list 만들었음

    ans_stack = []
    for i in number_list: # 후위표기법으로 표기한 number_list를 돌면서
        if i == '*':  # 만약에 * 를 만나면
            A = ans_stack[-2] * ans_stack[-1]  # 위에 두개 곱해주고
            ans_stack.pop()
            ans_stack.pop()  # 2개 pop해주고
            ans_stack.append(A) # 그 위에 다시 A 추가

        elif i =='+': # 만약 +를 만나도 똑같이
            A = ans_stack[-2] + ans_stack[-1]  # 위에 두개 더해주고
            ans_stack.pop()
            ans_stack.pop()  # 2개 pop해주고
            ans_stack.append(A) # 그 위에 다시 A 추가

        else: # 숫자인 경우는
            ans_stack.append(i)  #  스택에 추가

    print('#{} {}'.format(tc, ans_stack[0]))  # 다 끝나고 ans_stack에 남아있는 숫자 꺼내면 끝







