for tc in range(1, int(input())+1):
    A = list(input().split())
    number = []
    for a in range(len(A)):
        if A[a] == '+' or A[a] == '-' or A[a] == '*' or A[a] == '/' or A[a] == '.':
            number.append(A[a])
        else:
            N = int(A[a])
            number.append(N)

    stack = []
    answer = 0
    for i in number:
        if i == '+':
            if len(stack) > 1:
                answer = stack[-2] + stack[-1]
                stack.pop(-1)
                stack.pop(-1)
                stack.append(answer)
            else:
                print('#{} error'.format(tc))
                answer = 0
                break

        elif i == '-':
            if len(stack) > 1 :
                answer = stack[-2] - stack[-1]
                stack.pop(-1)
                stack.pop(-1)
                stack.append(answer)
            else:
                print('#{} error'.format(tc))
                answer = 0
                break

        elif i == '*':
            if len(stack) > 1 :
                answer = stack[-2] * stack[-1]
                stack.pop(-1)
                stack.pop(-1)
                stack.append(answer)
            else:
                print('#{} error'.format(tc))
                answer = 0
                break

        elif i == '/':
            if len(stack) > 1 :
                answer = stack[-2] / stack[-1]
                stack.pop(-1)
                stack.pop(-1)
                stack.append(answer)
            else:
                print('#{} error'.format(tc))
                answer = 0
                break
        elif i == '.':
            if len(stack) != 1:
                print('#{} error'.format(tc))
                answer = 0
                break

        else:
            stack.append(i)
    answer = int(answer)
    if answer:
        print('#{} {}'.format(tc, answer))