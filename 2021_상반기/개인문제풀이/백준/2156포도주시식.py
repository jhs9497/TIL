N = int(input())
dp = [0]*(N+1) # 0~i번째 상황에서 가장 최대의 와인을 선택할 때 총 와인량을 표시
wine = [0] # input받은 와인의 양을 나타낸 리스트
for _ in range(N):
    wine.append(int(input()))

if N <= 2: # 총 와인 수가 2보다 적은 경우면 그냥 합쳐서 프린트
    print(sum(wine))

else:
    dp[0] = 0 # i-3 인덱스를 활용해야 되기 때문에 0번째도 0으로 설정해준다.
    dp[1] = wine[1] # 1번째에서 최대의 경우는 1번째 wine을 선택하는 것
    dp[2] = wine[1] + wine[2] # 2번째에서 최대의 경우는 1번째, 2번째 wine을 모두 선택하는 것

    for i in range(3, N+1):
        # dp[2] 까지는 정해져 있으므로 dp[3]부터 bottom-up방식으로 축적해나가기
        case1 = dp[i-1]
        # wine[i]번 째에서 와인을 안 먹는 경우 -> dp[i-1] 그대로 적용
        case2 = dp[i-2] + wine[i]
        # wine[i]번 째에서 와인을 먹고, wine[i-1]은 안 먹는 경우
        case3 = dp[i-3]+wine[i-1]+wine[i]
        # wine[i]번 째 와인 먹고, wine[i-1]번 째 와인도 먹는 경우
        dp[i] = max(case1, case2, case3)
    print(dp[-1])







