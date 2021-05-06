N, M, L = map(int, input().split())
rest = list(map(int, input().split()))
rest.append(0)
rest.append(L-1)
rest.sort()

left = 0
right = L-1
answer = 0
while left <= right:
    mid = (left+right) // 2
    count = 0 # 설치한 휴게소의 수
    for i in range(1, len(rest)):
        if rest[i] - rest[i-1] > mid:
            count += (rest[i] - rest[i-1] -1)//mid

    if count > M:
        left = mid + 1
    else:
        answer = mid
        right = mid - 1

print(answer)