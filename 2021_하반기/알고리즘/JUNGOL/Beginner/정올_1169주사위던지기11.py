def case_1(idx):
    if idx == N:
        return
    for i in range(1, 7):
        arr[idx] = i
        if idx == N-1:
            print(*arr)
        else:
            case_1(idx+1)

def case_2(idx, b):
    if idx == N:
        return

    for i in range(b, 7):
        arr[idx] = i
        if idx == N-1:
            print(*arr)
        else:
            case_2(idx+1, i)

def case_3(idx):
    if idx == N:
        return

    for i in range(1, 7):
        arr[idx] = i
        if idx == N-1 and len(set(arr)) == N:
            print(*arr)
        else:
            case_3(idx+1)

N, M = map(int, input().split())

arr = [1] * N

if M == 1:
    case_1(0)

elif M == 2:
    case_2(0, 1)

elif M == 3:
    case_3(0)

