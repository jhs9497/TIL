import math

Prime_list = [2]

for i in range(3, int(1000000**(0.5)), 2):
    for p in Prime_list:
        if i % p == 0: # 한 번이라도 나누어 떨어지면
            break # 그만
    else:
        Prime_list.append(i)

for tc in range(1, int(input())+1):
    A = int(input())
    B = 1
    door = 1
    while door == 1:
        C = A*B
        if math.sqrt(C) % B == 0:
            door = 2
        else:
            B += 1

    print('#{} {}'.format(tc, B))