import math

start = int(input())
end = int(input())


def check(number):
    global count, min_number

    if number == 1:
        return
    
    N = int(math.sqrt(number))
    for j in range(2, N+1):
        if number % j == 0:
            return
    
    count += number
    if number < min_number:
        min_number = number


count = 0
min_number = 1e9
for i in range(start, end+1):
    check(i)

if count == 0:
    print(-1)
else:
    print(count)
    print(min_number)
