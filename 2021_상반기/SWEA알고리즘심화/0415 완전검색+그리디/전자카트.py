def perm(idx):
    global answer, cart
    if idx == len(A):
        SEL = sel[::]
        SEL.insert(0, 1)
        SEL.append(1)
        total = 0
        for i in range(len(SEL)-1):
            total += cart[SEL[i]-1][SEL[i+1]-1]
        if total < answer:
            answer = total

    else:
        for i in range(len(A)):
            if check[i] == 0:
                sel[idx] = A[i]
                check[i] = 1
                perm(idx+1)
                check[i] = 0

for tc in range(1, int(input())+1):
    N = int(input())
    cart = [list(map(int, input().split())) for _ in range(N)]

    A = []

    for i in range(2, N+1):
        A.append(i)

    sel = [0]*len(A)
    check = [0]*len(A)
    answer = 99**99
    perm(0)

    print('#{} {}'.format(tc, answer))