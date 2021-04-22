for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    C_info = [[] for _ in range(V)] # 연결 정보
    W_info = [[] for _ in range(V)] # 가중치 정보
    for i in range(E):
        data = list(map(int, input().split()))
        C_info[data[0]].append(data[1])
        W_info[data[0]].append(data[2])

    print(C_info)
    print(W_info)