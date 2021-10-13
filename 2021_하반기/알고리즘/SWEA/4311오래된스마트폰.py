tc = int(input())
for _ in range(tc):
    N, O, M = map(int, input().split())
    number_list = list(input().split())
    operator_list = []
    operator_input = list(map(int, input().split()))
    for o in operator_input:
        if o == 1:
            operator_list.append('+')
        elif o == 2:
            operator_list.append('-')
        elif o == 3:
            operator_list.append('*')
        else:
            operator_list.append('//')
    W = int(input())

