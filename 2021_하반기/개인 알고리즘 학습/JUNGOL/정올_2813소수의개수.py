import math

def check(i):
    global count
    sqrt = int(math.sqrt(i))
    for j in range(i**2, sqrt+1):
        if i % j == 0:
            return
    count += 1

M, N = map(int, input().split())

number_list = []
for i in range(M, N+1):
    number_list.append(0)

prime_list = [2,3,5,7]

for i in prime_list:
    for j in range(M, N+1):
        if j % i == 0:
            number_list[j-M] = 1

count = 0
for number in range(M, N+1):
    check(number)
