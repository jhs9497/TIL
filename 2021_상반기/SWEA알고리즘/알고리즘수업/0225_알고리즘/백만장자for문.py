import sys
sys.stdin = open("백만장자.txt")

for tc in range(1, int(input())+1):
    N = int(input())
    price = list(map(int, input().split()))

    profit = 0
    Max_price = price[N-1]  # 우선 시작점
    for i in range(N-1, -1, -1):
        if price[i] < Max_price: # 만약 뒤에서 현재 Max_price보다 작으면
            profit += Max_price - price[i]  # profit에 추가
        else: # price[i]가 크거나 같으면
            Max_price = price[i]  # Max_price교체

    print('#{} {}'.format(tc, profit))