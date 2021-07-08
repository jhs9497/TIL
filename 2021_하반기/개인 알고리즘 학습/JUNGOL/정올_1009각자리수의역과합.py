door = 'open'

while door == 'open':
    N = int(input())
    if N == 0:
        door = 'close'
    else:
        reverse = ''
        plus = 0
        while N > 0:
            number = N % 10
            N = N // 10
            if reverse =='' and str(number) =='0':
                pass
            else:
                reverse += str(number)
            plus += number

        print(reverse, plus)
