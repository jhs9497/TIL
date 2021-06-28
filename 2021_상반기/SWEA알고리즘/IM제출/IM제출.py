for tc in range(1, int(input())+1):
    N, M1, M2 = map(int, input().split())
    block = list(map(int, input().split()))

    block.sort()
    block.reverse()

    M1_list = []
    M2_list = []

    if M1 >= M2:

        for i in range(M2*2):
            if i % 2 == 1:
                M1_list.append(block[i])
            else:
                M2_list.append(block[i])

        for j in range(M2*2, len(block)):
            M1_list.append(block[j])

    else:
        for i in range(M1*2):
            if i % 2 == 1:
                M2_list.append(block[i])
            else:
                M1_list.append(block[i])

        for j in range(M1*2, len(block)):
            M2_list.append(block[j])

    ans = 0

    for i in range(len(M1_list)):
        ans += M1_list[i] * (i+1)

    for j in range(len(M2_list)):
        ans += M2_list[j] * (j+1)


    print("#%d %d" % (tc, ans))

