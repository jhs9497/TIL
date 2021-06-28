# N X N 짜리 바둑판을 우선 만들고

N = 5

answer = [[0 for _ in range(N)] for _ in range(N)]

my_pos = [0, 4]

left = [-1, 0]
right = [1, 0]
up = [0, 1]
down = [0, -1]

for i in range(N):
    answer[0][i] = i+1

print(answer)

play_list = [] # 횟수 리스트

for j in range(N-1, 0, -1):   # 44332211
    play_list += [j]
    play_list += [j]

number = N
for a in play_list:
    for b in range(a):
        number += 1
        if a % 2 == 0:
            my_pos[0] += down[0]
            my_pos[1] += down[1]
            number[my_pos[0]][my_pos[1]] = number


