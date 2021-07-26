def check_score(card_list):
    # 1번룰
    rule_one = True
    for i in range(len(card_list)-1):
        if card_list[i][0]+1 != card_list[i+1][0]:
            rule_one = False
        if card_list[i][1] != card_list[i+1][1]:
            rule_one = False

    if rule_one == True:
        return 900+card_list[-1][0]


    # 2번룰
    for i in range(len(card_list)):
        count = 0
        for j in range(len(card_list)):
            if card_list[i][0] == card_list[j][0]:
                count += 1

        if count == 4:
            return 800+card_list[i][0]


    # 3번룰
    number_count = [0]*10
    for i in range(len(card_list)):
        number_count[card_list[i][0]] += 1

    is_three = 0
    is_two = 0
    for j in range(len(number_count)):
        if number_count[j] == 3:
            is_three = j
        if number_count[j] == 2:
            is_two = j

    if is_three != 0 and is_two != 0:
        return 700 + is_three*10 + is_two

    # 4번룰
    color_count = [0]*4
    for i in range(len(card_list)):
        if card_list[i][1] == 'R':
            color_count[0] += 1
        elif card_list[i][1] == 'B':
            color_count[1] += 1
        elif card_list[i][1] == 'Y':
            color_count[2] += 1
        elif card_list[i][1] == 'G':
            color_count[3] += 1

    for x in color_count:
        if x == 5:
            return 600 + card_list[-1][0]

    # 5번룰
    rule_five = True
    for i in range(len(card_list)-1):
        if card_list[i][0]+1 != card_list[i+1][0]:
            rule_five = False

    if rule_five == True:
        return 500 + card_list[-1][0]

    # 6번룰 // 3번룰의 number_count 재활용
    is_three = 0
    for j in range(len(number_count)):
        if number_count[j] == 3:
            is_three = j

    if is_three != 0:
        return 400 + is_three

    # 7번룰
    is_two_small = 0
    is_two_big = 0
    for k in range(len(number_count)):
        if number_count[k] == 2:
            if is_two_small == 0:
                is_two_small = k
            else:
                is_two_big = k

    if is_two_small != 0 and is_two_big != 0:
        return 300 + is_two_big*10 + is_two_small

    # 8번룰
    is_two = 0
    for j in range(len(number_count)):
        if number_count[j] == 2:
            is_two = j

    if is_two != 0:
        return 200 + is_two

    # 9번룰
    return 100 + card_list[-1][0]



card_list = []
for _ in range(5):
    color, number = input().split()
    card_list.append((int(number), color))

card_list.sort()

score = check_score(card_list)
print(score)