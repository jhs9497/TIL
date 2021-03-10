K = 4
M = 5

N_list = []

for i in range(M):
    N = list(map(int, input().split()))
    N_list.append(N)

print(N_list)

info = [[] for _ in range(K+1)] # visted처럼 +1 해서 만들었고

for i in range(len(N_list)): # 0
    info[N_list[i][0]].append(N_list[i][1])
    info[N_list[i][1]].append(N_list[i][0])

print(info)