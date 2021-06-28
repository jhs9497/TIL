def preorder(X):
    global pre_answer
    if X > 0:
        pre_answer.append(X)
        preorder(left_C[X])
        preorder(right_C[X])

def postorder(X):
    global post_answer
    if X > 0:
        postorder(left_C[X])
        postorder(right_C[X])
        post_answer.append(X)

# nodeinfo = list(input().split(,))
nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]

# 2. 주어진 예시에 3번째 요소로 실제 노드의 값 추가

for idx in range(len(nodeinfo)):
    nodeinfo[idx] += [idx+1]

# x[1] == y를 내림차순, x[0] == x를 내림차순으로 정렬,
# 이제 test 리스트는 높이 순으로 정렬된 트리 구조가 됨
test = sorted(nodeinfo,key= lambda x : (-x[1],x[0]))

left_C = [0 for _ in range(1000)] # 왼쪽 촤일드
right_C = [0 for _ in range(1000)] # 오른쪽 촤일드

lay = []

for i in range(len(test)):
    lay.append(test[i][1])

lay = set(lay) # 중복 제거
lay = list(lay)
lay.reverse() # 다시 리스트화


for i in range(len(lay)-1):
    P = lay[i] # 부모 층 ? 높이 ? y값
    C = lay[i+1] # 촤일드 y값
    P_list = [] # X값
    C_list = []
    P_nod = [] # 내용물
    C_nod = []
    for j in range(len(test)):
        if test[j][1] == P:
            P_list.append(test[j][0])
            P_nod.append(test[j][2])
        if test[j][1] == C:
            C_list.append(test[j][0])
            C_nod.append(test[j][2])
    # C랑 제일 가까운 P 찾고 C가 P보다 작으면 왼쪽 촤일드 C가 P보다 크면 오른쪽 촤일드에 추가 . .?

    for a in range(len(C_list)):  # 촤일드 고정하고
        close = 9999999 # 제일 가까운 친구 찾기!
        idx = 0 # 그 때의 인덱스!
        for b in range(len(P_list)): # 부모랑 비교하면서
            if abs(C_list[a] - P_list[b]) < close:
                close = abs(C_list[a] - P_list[b])
                idx = b

        # idx를 단서로 X값을 비교한 후 레프트 촤일드에 추가할지 롸이트 촤일드에 추가할지 정한다1
        if C_list[a] < P_list[idx]: # 촤일드의 X값이 부모보다 작다는 것은
            left_C[P_nod[idx]] = C_nod[a] # 왼쪽에 추가!
        else:
            right_C[P_nod[idx]] = C_nod[a]

# print(left_C)
# print(right_C)

pre_answer = []
post_answer = []

preorder(test[0][2])
postorder(test[0][2])

result = [pre_answer, post_answer]

print(result)
