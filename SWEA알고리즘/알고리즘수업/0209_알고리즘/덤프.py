import sys
sys.stdin = open('box_dump.txt')


for tc in range(1, 11):
    X = 100 # 가로길이

    can_dump = int(input())

    box = list(map(int, input().split()))

    for dump in range(can_dump): # 횟수의 의미

        # dump 횟수만큼 max-1 min+1 하면서 최종 max와 min을 구하고 둘의 차를 구하자
        max_ = 0
        min_ = 999 # dump 한 번 돌릴 때 max_와 min_값을 구한다
        max_a = 0 # 그 때 박스의 인덱스값도 알아야함
        min_b = 0
        for i in range(len(box)):

            if max_ <= box[i]:
                max_ = box[i]
                max_a = i
            if min_ >= box[i]:
                min_ = box[i]
                min_b = i

        box_max = max_ - 1  # dump 한 번이 끝나면 맨 위에 최종 변수에
        box_min = min_ + 1  # max_와 min_값을 -1, +1 해서 입력
        box[max_a] = box_max
        box[min_b] = box_min  # 여기까지 box 정리 완료

    max_box = 0  # 정리된 box가지고 한번 더 max, min 구하고 차이 출력
    min_box = 9999
    for b in box:
        if max_box < b :
            max_box = b
        if min_box > b:
            min_box = b

    answer = max_box - min_box

    print('#{} {}'.format(tc, answer))







