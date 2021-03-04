for tc in range(1, int(input())+1):
    N = int(input())
    cordi = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if cordi[i][j] > 0: # 만약 화학물질을 처음으로 마주한다면
                dx = 1 # 우측으로 쭉쭉
                dy = 1 # 아래로 쭉쭉

                if 0 <= i+dx < N:
                    # i+dx가
