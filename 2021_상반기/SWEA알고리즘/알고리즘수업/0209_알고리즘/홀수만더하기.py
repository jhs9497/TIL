test_case = int(input())

for i in range(1, test_case +1):
    number = list(map(int, input().split()))

    count = 0
    for j in number:
        if j % 2 != 0:
            count += j
    print('#{} {}'.format(i, count))