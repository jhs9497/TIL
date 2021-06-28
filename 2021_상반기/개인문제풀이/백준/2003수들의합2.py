N, M = map(int, input().split())
numbers = list(map(int, input().split()))
S = 0
E = -1
Now = 0
Count = 0
while S < N:
    if Now < M:
        E += 1
        if E < N:
            Now += numbers[E]
    else:
        if Now == M:
            Count += 1
        S += 1
        if S < N:
            Now -= numbers[S-1]

    if E >= N:  # E가 끝까지 갔을 때
        S += 1
        if S < N:
            Now -= numbers[S-1]

print(Count)