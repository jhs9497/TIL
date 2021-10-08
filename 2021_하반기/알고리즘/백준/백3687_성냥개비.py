can_list = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

def cal_Max(c):
    answer = ''
    if c % 2 == 0:
        while c > 0:
            answer += '1'
            c -= 2
    else:
        answer += '7'
        c -= 3
        while c > 0:
            answer += '1'
            c -= 2
    return answer

def cal_Min(c):
    min_dict = {
        '2': '1',
        '3': '7',
        '4': '4',
        '5': '2',
        '6': '0',
        '7': '8'
    }
    if c == 2:
        return 1
    if c == 3:
        return 7
    if c == 4:
        return 4
    if c == 5:
        return 2
    if c == 6:
        return 6
    if c == 7:
        return 8
    if c == 8:
        return 10

    answer = '1'
    c -= 2
    while c > 0:
        if c - 7 > 1:
            answer += ''

    return answer

N = int(input())
for _ in range(N):
    count = int(input())
    Max_N = cal_Max(count)
    Min_N = cal_Min(count)
    print(Min_N, end=" ")
    print(Max_N)