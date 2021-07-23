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


#반복되는 구간 찾기 (ㄱ자구간 찾기)
side_one = 0
side_one = 0
for i in range(0, 3):
    if (direction_list[i], direction_list[i+1]) == (direction_list[i+2], direction_list[i+3]):
        side_one = i+1
        side_two = i+2

size = (max(length_list[0]) * max(length_list[1])) - (length_list2[side_one] * length_list2[side_two])

answer = size * N

print(answer)