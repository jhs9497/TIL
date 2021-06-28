def check(n):
    if n == 1 or n ==2:
        return 1
    return check(n-1) + check(n-2)

N = int(input())
road = list(map(int, input()))

answer = 1
count = 0
for i in range(len(road)):
    if road[i] == 1:
        count += 1
    elif road[i] == 0:
        answer = answer * check(count)
        count = 0

if count != 0:
    answer = answer * check(count)

print(answer)


