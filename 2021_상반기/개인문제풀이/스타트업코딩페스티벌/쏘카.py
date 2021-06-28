def check(X):

    New_T_list = []

    for i in range(len(T_list)):
        New_T = []
        fast_time = ''
        fast_time += T_list[i][0]
        fast_time += T_list[i][1]
        fast_time += T_list[i][3]
        fast_time += T_list[i][4]
        New_T.append(int(fast_time))
        late_time = ''
        late_time += T_list[i][8]
        late_time += T_list[i][9]
        late_time += T_list[i][11]
        late_time += T_list[i][12]
        New_T.append(int(late_time))
        New_T_list.append(New_T)

    answer_fast = 0
    answer_late = 9999
    for i in range(len(New_T_list)):
        if answer_fast < New_T_list[i][0]:
            answer_fast = New_T_list[i][0]

        if answer_late > New_T_list[i][1]:
            answer_late = New_T_list[i][1]
    

    if answer_fast > answer_late:
        return -1
    if answer_fast < 10:
        answer_fast = str(answer_fast)
        result = '00:0'
        result += answer_fast[0]
        result += ' '
        result += '~'
        result += ' '

    elif answer_fast < 100:
        answer_fast = str(answer_fast)
        result = '00:'
        result += answer_fast[0]
        result += answer_fast[1]
        result += ' '
        result += '~'
        result += ' '

    elif answer_fast < 1000:
        answer_fast = str(answer_fast)
        result = '0'
        result += answer_fast[0]
        result += ':'
        result += answer_fast[1]
        result += answer_fast[2]
        result += ' '
        result += '~'
        result += ' '
    else:
        result = ''
        answer_fast = str(answer_fast)
        result += answer_fast[0]
        result += answer_fast[1]
        result += ':'
        result += answer_fast[2]
        result += answer_fast[3]
        result += ' '
        result += '~'
        result += ' '

    if answer_late < 10:
        answer_late = str(answer_late)
        L_result = '00:0'
        L_result += answer_late[0]
        result += L_result

    elif answer_late < 100:
        answer_late = str(answer_late)
        L_result = '00:'
        L_result += answer_late[0]
        L_result += answer_late[1]
        result += L_result
    
    elif answer_late < 1000:
        result += '0'
        answer_late = str(answer_late)
        result += answer_late[0]
        result += ':'
        result += answer_late[1]
        result += answer_late[2]
    else:
        answer_late = str(answer_late)
        result += answer_late[0]
        result += answer_late[1]
        result += ':'
        result += answer_late[2]
        result += answer_late[3]



    if answer_fast == answer_late:
        result = result[0:5]
        return(result)
    else:
        return(result)


P = int(input())
T_list = []
for _ in range(P):
    T = input()
    T_list.append(T)

print(check(T_list))
