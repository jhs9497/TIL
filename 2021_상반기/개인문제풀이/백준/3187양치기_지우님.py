n,m = map(int,input().split())
arr = [list(input()) for _ in range(n)]
# print(arr) [['.', '.', '.', '#', '.', '.'], ['.', '#', '#', 'v', '#', '.'], ['#', 'v', '.', '#', '.', '#']]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
answer = {'v_cnt': 0, 'k_cnt': 0}
for r in range(n):
    for c in range(m):
        if arr[r][c] == 'k' or arr[r][c] == 'v':
            num = []
            stack = []
            num.append(arr[r][c])
            stack.append((r, c))
            while stack:
                r,c = stack.pop()
                arr[r][c] = '#'
                for di in range(4):
                    n_r = r + dr[di]
                    n_c = c + dc[di]
                    if 0 <= n_r < n and 0 <= n_c < m and arr[n_r][n_c] != '#':
                        stack.append((n_r, n_c))
                        if arr[n_r][n_c] == 'v' or arr[n_r][n_c] == 'k':
                            num.append(arr[n_r][n_c])
                        arr[n_r][n_c] = '#'
            v_cnt, k_cnt = 0,0
            for i in num:
                if i == 'v':
                    v_cnt += 1
                else:
                    k_cnt += 1
            if k_cnt > v_cnt:
                answer['k_cnt'] += k_cnt
            else:
                answer['v_cnt'] += v_cnt

print(answer['k_cnt'], answer['v_cnt'])
print(answer)