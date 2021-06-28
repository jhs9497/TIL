for tc in range(1, int(input())+1):
    two = list(input())
    three = list(input())
    door = 'O'  # 이중 for문 탈출을 위함
    for i in range(len(two) * 2):
        copy_two = two[:]
        copy_two[i // 2] = str(i % 2)
        a = int(''.join(copy_two), 2)
        for j in range(len(three) * 3):
            copy_three = three[:]
            copy_three[j // 3] = str(j % 3)
            b = int(''.join(copy_three), 3)
            if a == b:
                print('#{} {}'.format(tc, a))
                door = 'X'
                break
        if door == 'X':
            break
