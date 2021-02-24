for tc in range(1, int(input())+1):
    N = int(input()) # 인풋 받은 카드 갯수
    card = list(input().split())

    A_card = []
    B_card = []
    New_card = []
    if N % 2 == 0: # N이 짝수이면
        for i in range(N//2):
            A_card.append(card[i])
        for j in range(N//2, N):
            B_card.append(card[j])
        # 여기까지 카드 반으로 나눔
        for k in range(N//2):
            New_card.append(A_card[k])  # 차례대로 New_card에 추가
            New_card.append(B_card[k])

    else: # N이 홀수이면
        for i in range(N//2+1):
            A_card.append(card[i])
        for j in range(N//2+1, N):
            B_card.append(card[j])
        B_card.append('') # 짝수를 맞추기 위해 마지막에 빈공간 추가

        for k in range(N//2+1):
            New_card.append(A_card[k])  # 차례대로 New_card에 추가
            New_card.append(B_card[k])

    print('#{}'.format(tc), end = " ")
    print(*New_card)
