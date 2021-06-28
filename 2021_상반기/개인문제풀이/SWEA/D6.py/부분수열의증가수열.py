make = []

def DFS_a(level):
    sub_set = []
    if subset[level] == 1:
        sub_set.append(powerset[level])
        print(powerset[level])
    if level >= N:
        make.append(sub_set)
        return

    subset[level] = 0
    DFS_a(level + 1)
    subset[level] = 1
    DFS_a(level + 1)

for tc in range(1, int(input())+1):

    N, L = map(int, input().split())

    powerset = list(map(int, input().split()))

    subset = [0] * (N+1)

    DFS_a(0)

    print(make)