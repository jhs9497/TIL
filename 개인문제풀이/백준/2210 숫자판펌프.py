def BFS(x, y):
    answer = []
    queue = [(x, y)]
    while queue:
        x, y = queue.pop(0)
        for a in range(4):
            for b in range(4):
                for c in range(4):
                    for d in range(4):
                        for e in range(4):
                            for f in range(4):
                                for g in range(4):
                                    for h in range(4):
                                        for i in range(4):
                                            for j in range(4):
                                                if board[x + dx[a]+dx[c]+dx[e]+dx[g]+dx[i]][y + dy[b]+dy[d]+dy[f]+dy[h]+dy[j]] not in answer:
                                                    answer.append(board[x + dx[a]+dx[c]+dx[e]+dx[g]+dx[i]][y + dy[b]+dy[d]+dy[f]+dy[h]+dy[j]])










board = [list(map(int, input().split())) for _ in range(5)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

BFS(0,0)

