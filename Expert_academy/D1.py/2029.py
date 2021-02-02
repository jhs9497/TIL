test_case = int(input())

for i in range(test_case):

    numbers = list(map(int, input().split()))



    q, r = divmod(numbers[0], numbers[1])

    print(f'#{i+1} {q} {r}')