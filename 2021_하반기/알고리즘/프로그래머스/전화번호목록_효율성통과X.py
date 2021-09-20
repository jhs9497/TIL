def solution(phone_book):
    for i in range(len(phone_book)):
        for j in range(len(phone_book)):
            if i != j and phone_book[i] == phone_book[j][0:len(phone_book[i])]:
                return False

    answer = True
    return answer