N = int(input())

length_list = [[], []]

length_list2 = []
direction_list = []

max_length = 0
max_direction = 0
for _ in range(6):
    direction, length = map(int, input().split())
    if max_length < length:
        max_length = length
        max_direction = direction

    direction_list.append(direction)
    length_list2.append(length)

    # 남북 묶고
    if direction == 1 or direction == 2:
        length_list[0].append(length)

    # 동서 묶기
    else:
        length_list[1].append(length)



# 2개씩 나온 친구들 찾기
small_number_count = []
for i in range(1,5):
    if direction_list.count(i) == 2:
        small_number_count.append(i)

# 연속으로 나와 있는지 확인 후 일렬로 만들어주기

iscontinue = 0
for i in range(6):
    if direction_list[i] in small_number_count:
        iscontinue += 1
    if iscontinue != 0 and direction_list[i] not in small_number_count:
        break

small_number = []
if iscontinue == 4: # 쭉 이어져 있다는 소리
    for i in range(6):
        if direction_list[i] in small_number_count:
            small_number.append(length_list2[i])

else:
    for i in range(6):
        if direction_list[i] in small_number_count:
            if i == 0 or i == 1 or i == 2:
                small_number.append(length_list2[i])
            else:
                small_number.insert(0, length_list2[i])


size = (max(length_list[0]) * max(length_list[1])) - (small_number[1] * small_number[2])
answer = size * N
print(answer)
print(small_number_count)
print(length_list)
print(length_list2)
print(direction_list)
print(small_number)