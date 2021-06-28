for tc in range(1, 11):
    N = int(input())
    numbers = list(map(int, input().split()))

    while numbers[-1] >0:
        for i in range(5): # i로 인덱스와 빼는 값 모두 표현
            number = numbers[i] - (i+1) # number에 인덱스별로 빼고
            if number <= 0: # 만약 number가 0보다 작거나 같으면
                number = 0 # number는 0
                numbers.append(number)  # 추가하고
                break # 그만
            else:
                numbers.append(number) # numbers 뒤쪽에 어펜드

        # 뒷꼬리 추가 완료면 앞에 숫자 pop으로 없애주기
        if len(numbers) > 8:
            for i in range(len(numbers)-8):
                numbers.pop(0)

    # while문 끝나고 numbers print
    print('#{}'.format(N), end = ' ')
    print(*numbers)