test_case = int(input())

for tc in range(1, test_case+1):

    N = int(input())


    N_range = []
    for i in range(1, N+1):
        Ai, Bi = map(int, input().split()) 
        for x in range(Ai, Bi+1):
            N_range += [x]

    P = int(input())
    P_number = []
    for j in range(1, P+1):
        Cj = int(input())
        P_number += [Cj]

    total_count = ''
    for a in P_number:
        a_count = 0
        for b in range(len(N_range)):
            if a == N_range[b]:
                a_count += 1

        total_count += str(a_count)
        total_count += ' '

    print('#{} {}'.format(tc, total_count))