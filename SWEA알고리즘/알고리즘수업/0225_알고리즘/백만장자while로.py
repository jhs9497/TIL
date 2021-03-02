# 가장 비싼 가격이 있으면 그 가격 기준 왼쪽은 다 구매해서 이 날 팔아버리면 된다
# 가장 비싼 가격을 찾고 이미 판 리스트는 슬라이스로 제외시키자

import sys
sys.stdin = open("백만장자.txt")


for tc in range(1, int(input())+1):
    N = int(input())
    price = list(map(int, input().split()))

    total_profit = 0
    i = 0  # 슬라이스 시작점
    while i < N:
        profit = 0  # 단기 수익
        count = 0 # 나중에 pop할 용도
        M_P = max(price[i:N])  # 정해진 범위의 price에서 가장 큰 값을 정하고
        for p in price[i:N]: # 그 범위의 price를 돌면서
            count += 1 # count에 우선 더하고 (슬라이싱 시작점체크의 용도 + 계산용도)
            profit += p # profit에 우선 다 더하고  M_P도 우선 들어가긴함 M_P여도 우선 구입하고 수익0으로 판다는 마인드
            if p == M_P: # 팔 떄가 다가왔을때
                profit = M_P*(count) - profit # 지금까지 구매한 물건들 팔아버리고
                break
        # 계산이 끝났으면 총수익에 단기수익 더해주고
        total_profit += profit
        i += count # 슬라이스 시작점 지정

    print('#{} {}'.format(tc, total_profit))



