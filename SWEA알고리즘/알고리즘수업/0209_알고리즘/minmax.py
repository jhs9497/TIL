test_case = int(input())

for i in range(1, test_case+1):
    X = int(input())
    number = list(map(int, input().split()))

    max = 0
    min = 1000000

    for a in number:
        if max < a:
            max = a
        if min > a:
            min = a

    answer = max-min

    print('#{} {}'.format(i, answer))

