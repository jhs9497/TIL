N = int(input())

stack = [] # 숫자들을 쌓아줄 stack 선언
for i in range(N):
    input_value = list(input().split())
    if input_value[0] == 'i': # 인풋값의 첫번째 값이 i이면
        stack.append(input_value[1]) # 스택에 숫자 쌓아주고
    elif input_value[0] == 'o': # o이면
        if stack: # stack에 뭐라도 있을 경우
            print(stack.pop(0)) # 스택에 맨 앞에 있는 친구 뺌과 동시에 출력
        else: # stack에 아무것도 없을 경우
            print('empty') # empty 출력
    elif input_value[0] == 'c': # input값이 c이면
        print(len(stack)) # stack 길이 출력
