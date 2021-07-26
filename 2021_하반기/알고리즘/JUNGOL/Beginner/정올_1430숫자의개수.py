A = int(input())
B = int(input())
C = int(input())

number = A*B*C

number = str(number)

count_number = [0]*10

for num in number:
    count_number[int(num)] += 1

for answer in count_number:
    print(answer)