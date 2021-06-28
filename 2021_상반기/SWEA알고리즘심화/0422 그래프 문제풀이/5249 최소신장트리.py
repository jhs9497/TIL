'''
4 7
0 1 9
0 2 3
0 3 7
1 4 2
2 3 8
2 4 1
3 4 8
'''

from queue import PriorityQueue

def prime(s):
    global count

    D[s][0] = 0
    D[s][1] = 0

    for k in range(N+1):
        minV = 1000000
        for i in range(N+1):
            if i in U:
                continue
            if D[i][0] < minV:
                curV = i
                minV = D[i][0]
        U.append(curV)
        count += minV

        for w, dis in adj[curV]:
            if w in U:
                continue
            if D[w][0] > dis:
                D[w][0] = dis
                D[w][1] = curV


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    adj = [[] for _ in range(N + 1)]
    for i in range(M):
        S, E, V = map(int, input().split())
        adj[S].append([E, V])
        adj[E].append([S, V])


    D = [[1000000, -1] for _ in range(N+1)]

    U = []
    count = 0
    prime(0)

    print('#{} {}'.format(tc, count))


