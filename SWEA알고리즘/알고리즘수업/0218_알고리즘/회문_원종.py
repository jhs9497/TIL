T = int(input())
for test in range(1, T+1):


    n, m = map(int, input().split())

    arr = [list(input().split()) for _ in range(n)]
    arr_real = [[''] * n for _ in range(n)]
    for a in range(n):
        A = ''.join(arr[a])
        for b in range(len(A)):
            arr_real[a][b] = A[b]
    arr = arr_real
    result = []
#     행 우선
    rever = []
    for i in range(n):
        b = arr[i][::-1]
        rever.append(b)

    for z in range(n):

        for i in range(n-m+1):
            cnt = 0
            for j in range(m):
                if arr[z][i+j] == rever[z][j]:
                    cnt += 1
                    if cnt == m:
                        for k in range(m):
                            result.append(arr[z][k])


    # 열 우선
    yol = []
    for c in range(n):
        sub = []
        for r in range(n):
            sub.append(arr[r][c])
        yol.append(sub)
    #열 반대로 돌려버리기
    yolrever = []
    for i in range(n):
        q = yol[i][::-1]
        yolrever.append(q)

    for i in range(n):

        for j in range(n-m+1):
            cnt = 0
            for x in range(m):
                if yol[i][j+x] == yolrever[i][x]:
                    cnt += 1
                    if cnt == m:
                        for k in range(m):
                            result.append(yol[i][k])



    print("#{} {}".format(test, ''.join(result)))