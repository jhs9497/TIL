from itertools import permutations

def permu():
    number_list = [x for x in range(1, N)]
    permu_list = list(permutations(number_list, M - 1))
    answer = 1e10
    for i in range(len(permu_list)):
        temp_max = 0
        for j in range(len(permu_list[i])):
            temp_answer = 0
            if j == 0:
                for k in range(0, permu_list[i][j]):
                    temp_answer += bead_list[k]

            elif j == len(permu_list[i]) - 1:
                A_answer = 0
                for a in range(permu_list[i][j], N):
                    A_answer += bead_list[a]

                B_answer = 0
                for b in range(permu_list[i][j - 1], permu_list[i][j]):
                    B_answer += bead_list[b]

                temp_answer = max(A_answer, B_answer)

            else:
                for k in range(permu_list[i][j - 1], permu_list[i][j]):
                    temp_answer += bead_list[k]

            if temp_max < temp_answer:
                temp_max = temp_answer

        if answer > temp_max:
            answer = temp_max

    return answer


N, M = map(int, input().split())
bead_list = list(map(int, input().split()))

if M > 2:
    answer = permu()
    print(answer)
else:
    number_list = [x for x in range(1, N)]
    answer = 1e10
    for n in number_list:
        temp_max = 0
        temp_front = 0
        temp_back = 0
        for x in range(0, n):
            temp_front += bead_list[x]
        for y in range(n, N):
            temp_back += bead_list[y]
        temp_max = max(temp_front, temp_back)
        if answer > temp_max:
            answer = temp_max

    print(answer)

