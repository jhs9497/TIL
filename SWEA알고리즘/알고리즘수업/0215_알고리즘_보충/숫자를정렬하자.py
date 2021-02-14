import sys
sys.stdin = open("정렬.txt","r")

test_case = int(input())

for tc in range(1, test_case+1):
    N = int(input())
    number = list(map(int, input().split()))

    for i in range(len(number)):
        for j in range(len(number)-1):
            if number[j] >= number[j+1]:
                number[j], number[j+1] = number[j+1], number[j]

    answer = ''
    for z in range(len(number)):
        answer += str(number[z])
        answer += ' '

    print("#{} {}".format(tc, answer))
