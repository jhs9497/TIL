def parent1(N):
    global N1_parent
    if N == 1:
        return
    for i in range(len(con)):
        if N in con[i]:
            N1_parent.append(i)
            parent1(i)

def parent2(N):
    global N2_parent
    if N == 1:
        return
    for i in range(len(con)):
        if N in con[i]:
            N2_parent.append(i)
            parent2(i)

def common(N1, N2):
    for i in N1:
        for j in N2:
            if i == j:
                return i

def tree(root):
    global count
    if root > 0:
        count += 1
        tree(con[root][0])
        tree(con[root][1])


for tc in range(1, int(input())+1):
    V, E, N1, N2 = map(int, input().split())
    info = list(map(int, input().split()))
    con = [[0,0] for _ in range(V+1)]
    for i in range(0, len(info), 2):
        if con[info[i]][0] == 0:
            con[info[i]][0] = info[i+1]
        else:
            con[info[i]][1] = info[i+1]

    N1_parent = [] # N1 조상 리스트
    parent1(N1) # N1 조상 찾는 함수
    N2_parent = [] # N2 조상 리스트
    parent2(N2) # N2 조상 찾는 함수
    com_parent = common(N1_parent, N2_parent) # 서로 공통적이며 가장 가까운 조상찾는 함수
    count = 0 # 최종 카운트
    tree(com_parent) # 그 조상 기준으로 서브트리 개수 구하는 함수
    print("#{} {} {}".format(tc, com_parent, count))