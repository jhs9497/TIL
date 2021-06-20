def solution(S, C):
    email_list = []
    name_list = list(S.split(';'))
    for each_name in name_list:
        name = list(each_name.split())
        first = name[0].lower()
        last = name[-1].lower().replace('-', '')
        last = last.replace(';', '')
        last = last[:8]
        final_name = first + '.' + last

        door = 'open'
        N = 2
        while door == 'open':
            if final_name not in email_list:
                email_list.append(final_name)
                door = 'close'
            else:
                if final_name[-1].isdigit():
                    temp_N = N - 1
                    final_name = final_name.replace(str(temp_N), '')
                    final_name = final_name + str(N)
                    N += 1
                else:
                    final_name = final_name + str(N)
                    N += 1

    final_list = []
    for i in range(len(email_list)):
        if i == len(email_list) - 1:
            email_adress = name_list[i] + ' ' + '<' + email_list[i] + '@' + C.lower() + '.com>'
        else:
            email_adress = name_list[i] + ' ' + '<' + email_list[i] + '@' + C.lower() + '.com>;'
        final_list.append(email_adress)

    answer = ''
    for final in final_list:
        answer = answer + final + ''
    return answer