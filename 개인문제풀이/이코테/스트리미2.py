def reverse_str(word):
    flag = 'open'
    answer = ''
    temp = ''
    for alpha in word:
        if alpha != ' ':
            temp += alpha
        elif alpha == ' ':
            if flag == 'open':
                answer = temp
                temp = ''
                flag = 'close'
            else:
                answer = temp + ' ' + answer
                temp = ''
    answer = temp + ' ' + answer

    print(answer, len(answer))

reverse_str('SAFFY JOB FAIR')