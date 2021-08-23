def check_id(new_id):
    str_list = ['-', '_', '.']

    if not 3 <= len(new_id) <= 15:
        return False

    if new_id[0] == '.' or new_id[-1] == '.':
        return False

    for i in range(len(new_id)):
        if new_id[i].islower() == False:
            return False

        if new_id[i].isdigit() == False:
            return False

        if new_id[i] not in str_list:
            return False

        if new_id[i] == '.':
            if new_id[i + 1] == '.':
                return False

    return True


def solution(new_id):
    flag = check_id(new_id)
    # if flag == True:
    #     answer = new_id
    #     return answer
    return flag