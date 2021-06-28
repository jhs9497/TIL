for tc in range(1, int(input())+1):
    number = float(input())
    answer = ''
    count = 0
    while number != 0 and count < 13:
        number = number * 2
        if number >= 1:
            answer += '1'
            number -= 1
        else:
            answer += '0'
        count += 1

    if count == 13:
        print('#{} overflow'.format(tc))
    else:
        print('#{} {}'.format(tc, answer))