def floatToString(n):
    if n == int(n):
        answer = int(n)
    if n > 0:
        int_number = int(n)
        answer = str(int_number) + '.'
        float_number = n - int(n)
        float_number = float_number * 1e15
        float_number = str(float_number)
        count = 0
        temp = ''
        for i in float_number:
            temp += i
            count += 1
            if n > 0:
                if n - (int(temp) / 10**count) == int(n):
                    answer += temp
                    break
        print(answer)
    else:
        int_number = int(n)
        answer = str(int_number) + '.'
        float_number = int(n) - n
        float_number = float_number * 1e15
        float_number = str(float_number)
        count = 0
        temp = ''
        for i in float_number:
            temp += i
            count += 1
            if n + (int(temp) / 10**count) == int(n):
                answer += temp
                break
        print(answer)

floatToString(10.909)
