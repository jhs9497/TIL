N = int(input())

snail = [[0]*N for _ in range(N)]

input_number = 1
d = 1
x, y = 0, -1
for _ in range(N):
    number = 2*N -1
    count = 0
    while count < number:
        if count <= number // 2:
            x, y = x, y + d
            snail[x][y] = input_number

        else:
            x, y = x + d, y
            snail[x][y] = input_number

        count += 1
        input_number += 1
    d *= -1
    N -= 1

for i in snail:
    print(*i)