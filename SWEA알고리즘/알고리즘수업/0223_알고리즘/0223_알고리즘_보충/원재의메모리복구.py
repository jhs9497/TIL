# 우선 가장 왼쪽의 1을 찾고!
# 1 -> 0으로 바뀌는 순간이나 0 -> 1로 바뀌는 순간 모두 count +1

for tc in range(1, int(input())+1):
    memory = input()

    count = 0
    idx = 0
    for i in range(len(memory)):
        if memory[i] == '1': # 가장 왼쪽부터 해서 1을 찾으면!
            count += 1 # 우선 count +1 해주고
            idx = i # 그 idx 박제하고
            break# 그만!

    # 1의 시작점 idx부터 다시 for문을 돌리며
    for j in range(idx, len(memory)-1):
        if memory[j] != memory[j+1]: count += 1
        # memory 값이 바뀌는 순간 count +1
    print('#{} {}'.format(tc, count))

