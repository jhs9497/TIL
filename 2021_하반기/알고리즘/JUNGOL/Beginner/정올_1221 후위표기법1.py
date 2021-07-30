N = int(input())
number_list = list(input().split())

number_stack = []

for value in number_list:
    if value == '+':
        A = number_stack.pop()
        B = number_stack.pop()
        number = A + B
        number_stack.append(number)

    elif value == '-':
        A = number_stack.pop()
        B = number_stack.pop()
        number = B - A
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

    else:
        number_stack.append(int(value))

print(int(number_stack[0]))