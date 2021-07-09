import math

def check_down(N):
    global number_list
    for i in range(N, 0, -1):
        k = int(math.sqrt(i))
        door = 'open'
        for j in range(2, k+1):
            if i % j == 0:
                door = 'close'
                break

        if door == 'open':
            number_list.append(i)
            return


def check_up(N):
    global number_list
    for i in range(N+1, 1000001):
        k = int(math.sqrt(i))
        door = 'open'
        for j in range(2, k + 1):
            if i % j == 0:
                door = 'close'
                break

        if door == 'open':
            number_list.append(i)
            return


T = int(input())

for _ in range(T):
    number_list = []
    N = int(input())
    check_down(N)
    check_up(N)

    if len(number_list) == 1:
        print(number_list[0])
    else:
        if abs(number_list[0] - N) < abs(number_list[1]-N):
            print(number_list[0])
        elif abs(number_list[0] - N) > abs(number_list[1]-N):
            print(number_list[1])
        else:
            print(number_list[0], number_list[1])