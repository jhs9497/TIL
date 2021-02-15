
for tc in range(10):
    N = int(input())

    number = []

    for _ in range(100):

        number.append(list(map(int, input().split())))

    sum_number_list = []

    # 행 더해서 추가
    for i in range(len(number)):
        sum_number = 0
        for j in range(len(number)):
            sum_number += number[i][j]
        sum_number_list += [sum_number]


    # 열 더해서 추가
    for i in range(len(number)):
        sum_number = 0
        for j in range(len(number)):
            sum_number += number[j][i]
        sum_number_list += [sum_number]

    # 우하향 대각선 추가

    sum_number = 0
    for i in range(len(number)):
        for j in range(len(number)):
            if i == j:
                sum_number += number[i][j]
    sum_number_list += [sum_number]

    # 좌하향 대각선 추가

    sum_number = 0
    for i in range(len(number)):
        for j in range(len(number)):
            if i + j == 99:
                sum_number += number[i][j]
    sum_number_list += [sum_number]


    answer = 0

    for x in sum_number_list:
        if answer < x:
            answer = x
    print("#{} {}".format(N, answer))


