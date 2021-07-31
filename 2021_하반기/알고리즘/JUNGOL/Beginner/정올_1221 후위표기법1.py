N = int(input())
number_list = list(input().split())

number_stack = []

for value in number_list:
    if value == '+': # 만약 + 면
        A = number_stack.pop() # 스택에 맨 뒤 A로 설정 & stack에서 제거
        B = number_stack.pop() # 스택에서 A 나가고 난 뒤 그 다음 친구 B로 설정 & stack에서 제거
        number = A + B # A + B 후
        number_stack.append(number) # 다시 stack에 넣어주기

    elif value == '-':
        A = number_stack.pop()
        B = number_stack.pop()
        number = B - A # 같은 과정이지만 - 와 / 는 B가 앞인 부분 유의
        number_stack.append(number)

    elif value == '*':
        A = number_stack.pop()
        B = number_stack.pop()
        number = A * B
        number_stack.append(number)

    elif value == '/':
        A = number_stack.pop()
        B = number_stack.pop()
        number = B / A
        number_stack.append(number)

    else: # 숫자인 경우 int화 해서 stackdp 추가해주기
        number_stack.append(int(value))

print(int(number_stack[0])) # 마지막까지 남아있는 친구 출력