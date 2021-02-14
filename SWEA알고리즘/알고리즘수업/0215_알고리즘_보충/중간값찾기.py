test_case = int(input())

number = list(map(int, input().split()))


for i in range(len(number)):
    for j in range(len(number)-1):
        if number[j] > number[j+1]:
            number[j], number[j+1] = number[j+1], number[j]

m = len(number) //2

answer = number[m]

print(answer)

