test_case = int(input())

for i in range(1, test_case +1):
    number = int(input())

    count = 0
    for j in range(number +1):
        if j % 2 == 1:
            count += j
        if j % 2 == 0:
            count -= j

    print('#{} {}'.format(i, count))