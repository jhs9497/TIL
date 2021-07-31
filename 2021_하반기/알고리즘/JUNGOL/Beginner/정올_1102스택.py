N = int(input())

stack = [] # 숫자들을 쌓아줄 stack 선언
for i in range(N):
    input_value = list(input().split()) # i의 경우 숫자가 뒤에 붙으므로 리스트로 받아주기
    if input_value[0] == 'i': # 만약 i가 인풋값이면
        stack.append(input_value[1]) # stack에 쌓아주기
    elif input_value[0] == 'o': # o가 인풋값이면
        if stack: # 만약 stack에 뭐라도 있을 경우에
            print(stack.pop()) # stack 맨 위에 있는 친구를 빼면서 프린트
        else: # stack에 아무것도 없으면
            print('empty') # emtpy 출력
    elif input_value[0] == 'c': # c가 인풋값이면
        print(len(stack)) # stack 길이 세서 출력
