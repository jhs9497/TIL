def cal(X, L, R):
    if X == '+':
        return L + R
    elif X == '*':
        return L * R
    elif X == '-':
        return L - R
    elif X == '/':
        return L / R

def check(root):
    if left_C[root] == 0 and right_C[root] == 0:
        return int(tree[root])
    if root > 0:
        L = check(left_C[root])
        R = check(right_C[root])
        tree[root] = cal((tree[root]), L, R)
    return tree[root]


for tc in range(1, 11):
    N = int(input())
    tree = [''] * (N+1)

    left_C = [0] * (N+1)
    right_C = [0] * (N+1)
    for i in range(N):
        inp = list(input().split())
        tree[int(inp[0])] = inp[1]

        if len(inp) > 2:
            left_C[int(inp[0])] = int(inp[2])
            right_C[int(inp[0])] = int(inp[3])

    cal_list = [0]
    check(1)

    print('#{} {}'.format(tc, int(tree[1])))



