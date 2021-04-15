# level : 몇 번째 선택을 하는 것인가! / 깊이
# S : 시작점
def combi(level, S):
    # 종료조건
    if level == K:
        print(arr)
        check(arr)
        return

    for i in range(S, N - K + level + 1):  # N=5, K=3, level=0 S~2
        arr[level] = box[i]
        combi(level + 1, i + 1)  # N=5, K=3, level=1 S~3
        # N=5, K=3, level=2 S~4

def check(arr):
    global answer
    timetable = [False]* 24
    for i in range(len(arr)):
        for j in range(arr[i][0], arr[i][1]):
            if timetable[j] == True:
                return
            else:
                timetable[j] = True

    answer = len(arr)
    return


for tc in range(1, int(input())+1):
    N = int(input())
    box = []
    for i in range(N):
        box.append(list(map(int, input().split())))

    answer = 0
    K = len(box)
    while answer == 0:
        arr = [0]*K
        combi(0,0)
        K -= 1

    print('#{} {}'.format(tc, answer))