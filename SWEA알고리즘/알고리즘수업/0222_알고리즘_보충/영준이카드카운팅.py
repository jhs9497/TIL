
def check_card():
    for i in range(4):
        for j in range(1, 13+1):
            if count[i][j] > 1 :  # 중복될 때
                return 0 # 중복되면 바로 끝!
            elif count[i][j] == 1: # 해당카드 무늬 세기
                ans[i] += 1 # 만들어둔 리스트에 추가
    return 1 # 여기까지 온건 중복없이 다 돈 것

for tc in range(1, int(input())+1):
    card = input()
    count = [[0] * 14 for _ in range(4)]
    ans = [0] * 4
    flag = 1  # True 라고 써도 됨 중복 체크 위한 것 1이냐 0이냐

    for i in range(0, len(card), 3):
        row = 0
        sdhc = card[i]
        col = int(card[i+1] + card[i+2])

        if sdhc == 'S' : row = 0
        elif sdhc == 'D' : row = 1
        elif sdhc == 'H' : row = 2
        elif sdhc == 'C' : row = 3

        count[row][col] += 1

    flag = check_card()

    print('#{}'.format(tc), end=" ") # 이어서
    if flag == 0: print("ERROR", end=" ")
    else:
        for i in range(4):
            print(13-ans[i], end=" ")
    print() # 줄바꿈

