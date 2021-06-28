for tc in range(1, int(input())+1):
    N = int(input())
    box = []
    for i in range(N):
        box.append(list(map(int, input().split())))
        box[i][0], box[i][1] = box[i][1], box[i][0]
    box.sort()

    count = 0
    timetable = [False] * 24
    for i in range(len(box)):
        flag = 'YES'
        for j in range(box[i][1], box[i][0]):
            if timetable[j] == True:
                flag = 'NO'
                break
            else:
                timetable[j] = True
        if flag == 'YES':
            count += 1

    print('#{} {}'.format(tc, count))
