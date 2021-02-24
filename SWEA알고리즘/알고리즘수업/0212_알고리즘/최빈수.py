import sys
sys.stdin = open("최빈수.txt", "r")



T = int(input())

for tc in range(T):
    N = int(input())
    number = list(map(int, input().split()))

    count_number = [0]*101

    for i in number:
        count_number[i] += 1

    answer_index = 0
    answer = 0
    for z in range(len(count_number)):
        if answer_index <= count_number[z]:
            answer_index = count_number[z]
            answer = z

    # answer = 0
    # for a in range(len(count_number)):
    #     if count_number[a] == answer_index:
    #         answer = a

    print("#{} {}".format(N, answer))