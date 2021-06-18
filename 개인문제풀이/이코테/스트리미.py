def function(n):
    flag = 'open'
    str_number = str(n)
    list_number = list(str_number)
    if list_number[0] == '-':
        list_number.pop(0)
        for i in range(len(list_number)):
            if 7 <= int(list_number[i]):
                list_number.insert(i, '7')
                flag = 'close'
                break

        if flag == 'open':
            list_number.append('7')

        answer = '-'
        for number in list_number:
            answer += number
        print(answer)
        return answer

    else:
        for i in range(len(list_number)):
            if 7 >= int(list_number[i]):
                list_number.insert(i, '7')
                break

        answer = ''
        for number in list_number:
            answer += number
        print(answer)

function(8888888)