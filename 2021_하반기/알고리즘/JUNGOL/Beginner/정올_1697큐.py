N = int(input())

stack = []
for i in range(N):
    input_value = list(input().split())
    if input_value[0] == 'i':
        stack.append(input_value[1])
    elif input_value[0] == 'o':
        if stack:
            print(stack.pop(0))
        else:
            print('empty')
    elif input_value[0] == 'c':
        print(len(stack))
