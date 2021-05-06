N, C = map(int, input().split())

Home = []

for _ in range(N):
    Home.append(int(input()))

Home.sort()

Left = 1
Right = Home[-1] - Home[0]
answer = 0

while Left <= Right:
    Mid = (Left + Right) // 2
    idx, count = 0, 1 # 왜 count가 1부터 시작하는지 ? ?

    for i in range(1, len(Home)):
        if Home[i] >= Home[idx] + Mid:
            idx = i
            count += 1

    if count < C: # 설치한 공유기 갯수가 설치해야할 공유기 수보다 적으면
                  # 설정한 mid값을 줄여야 하므로
        Right = Mid - 1

    else: # count > C보다 커지면  ??
        answer = Mid # 잠정적 답으로 저장하고
        Left = Mid + 1 # Mid값이 더 큰 경우 탐색

print(answer)