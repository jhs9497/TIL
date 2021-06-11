N, M = map(int, input().split())
card = []
# card 변수에 N(행) 길이만큼 for문 돌리면서 input값을 리스트화해서 추가해준다.
for _ in range(N):
    card.append(list(map(int, input().split())))

ans = 0 # 정답이 될 변수, 숫자는 1~10000의 범위라고 했으니 충분히 작은 0으로 초기설정
for number in card:
    # number는 각 행의 정보를 담고 있음
    # 만약 각행의 숫자중 가장 작은수보다 ans가 작다면 ans갱신
    # for문으로 계속 반복하다보면 각행별로 가장 작은 숫자 중 가장 큰 숫자를 구할 수 있다.
    if ans < min(number):
        ans = min(number)
print(ans)
