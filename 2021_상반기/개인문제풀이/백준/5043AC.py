from collections import deque

def check(func, number):
    Number = number
    for i in func:
        if i == 'R':
            Number.reverse()
        elif i == 'D':
            if len(Number) == 0:
                return 'error'
            Number.popleft()

    return Number

for tc in range(1, int(input())+1):
    func = input()
    func = deque(func)
    N = int(input())
    number = eval(input())  # 오호
    number = deque(number)

    answer = check(func, number)
    if answer == 'error':
        print('error')
    else:
        print(*answer)





