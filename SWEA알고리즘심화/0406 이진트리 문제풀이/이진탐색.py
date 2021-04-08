def tree(root):
    global answer
    global number
    if root > 0:
        tree(left_C[root])
        number += 1
        answer[root] = number
        tree(right_C[root])

for tc in range(1, int(input())+1):
    N = int(input())
    left_C = [0] * (N+1)
    right_C = [0] * (N+1)

    square = -1 # N이 2의 몇 제곱과 2의 몇제곱 사이에 있는지 알아내기 위함
    n = N
    while n > 0:
        n = n // 2
        square += 1

    for i in range(1, 2**(square-1)):
        left_C[i] = 2*i
        right_C[i] = (2*i) + 1

    for i in range(2**(square-1), N+1):
        # print(i)
        for j in range(i, N+1):
            if j == 2*i:
                left_C[i] = j
            if j == (2*i) +1:
                right_C[i] = j

    answer = [0] * (N+1)
    number = 0
    N_idx = N // 2

    tree(1)
    print('#{} {} {}'.format(tc, answer[1], answer[N_idx]))