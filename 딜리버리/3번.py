from itertools import permutations

def solution(N):
    # write your code in Python 3.6
    number_list = []
    for i in range(1, N+1, 2):
        number_list.append(i)

    for i in range(len(number_list)-1, 0, -1):
        temp_list = list(permutations(number_list, i))
        for j in range(len(temp_list)):
            number = 0
            for k in temp_list[j]:
                number += k
            if number == N:
                answer = list(temp_list[j])
                answer.sort()
                print(answer)
                return answer

solution(15)