N = int(input())
M = int(input())
combi_list = []
middle_component_list = []
for _ in range(M):
    X, Y, K = input().split()
    combi_list.append((int(X),int(Y),int(K)))
    middle_component_list.append(int(X))
combi_list.sort()
component_count = [0] * (N+1)

def check_count(a, b, c, k):
    if b not in middle_component_list:
        component_count[b] += c * k

    else:
        for i in range(M):
            if combi_list[i][0] == b:
                check_count(combi_list[i][0], combi_list[i][1], combi_list[i][2], c*k)

for i in range(M):
    if combi_list[i][0] == N:
        check_count(combi_list[i][0], combi_list[i][1], combi_list[i][2], 1)

for i in range(1, len(component_count)):
    if component_count[i] > 0:
        print(i, component_count[i])