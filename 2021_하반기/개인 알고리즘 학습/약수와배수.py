N = int(input())
number_list = list(map(int, input().split()))
number = int(input())

divisor = []
multiple = []

for i in number_list:
    if number % i == 0:
        divisor.append(i)

    if i % number == 0:
        multiple.append(i)

print(sum(divisor))
print(sum(multiple))