n, m = map(int, input().split())

if n % 2 == 0 or n < 1 or n > 100 or m < 1 or m > 3:
    print('INPUT ERROR!')

else:
    if m == 1:
        number = 1
        for i in range(1, n+1):
            answer = ''
            for j in range(i):
                if i % 2 == 1:
                    answer = answer + str(number) + ' '
                    number += 1

                elif i % 2 == 0:
                    answer = str(number) + ' ' + answer
                    number += 1
            print(answer)

    elif m == 2:
        number = 0
        count = 2 * n - 1
        while number < n:
            answer = ' ' * number * 2 + (str(number) + ' ') * count
            print(answer)
            number += 1
            count -= 2

    elif m == 3:
        number = 1
        for i in range(n):
            answer = ''
            for j in range(1, number+1):
                answer += str(j) + ' '

            if i < n // 2:
                number += 1
            else:
                number -= 1
            print(answer)

