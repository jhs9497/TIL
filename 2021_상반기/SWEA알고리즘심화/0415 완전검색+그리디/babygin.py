def babygin(card, who):
    global winner
    count = 0
    for i in range(len(card)):
        if card[i] >= 3:  # 중복된 3개 갖고있는지 췌크
            if who == 'A':
                winner = 1
                return
            else:
                winner = 2
                return

        if card[i] != 0:
            count += 1   # 연속된 3개의 숫자 갖고 있는지 췌크
        else:
            count = 0
        if count == 3:
            if who == 'A':
                winner = 1
                return
            else:
                winner = 2
                return

for tc in range(1, int(input())+1):
    card = list(map(int, input().split()))
    A_card = [0]*10
    B_card = [0]*10
    winner = 0
    for i in range(len(card)):
        if i % 2 == 0:
            A_card[card[i]] += 1
            if i >= 4:
                babygin(A_card, 'A')
        else:
            B_card[card[i]] += 1
            if i >= 5:
                babygin(B_card, 'B')

        if winner != 0:
            break

    print('#{} {}'.format(tc, winner))